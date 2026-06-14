import Plausible
/-! # Searching for MISSING F1 with Plausible

The argmax decision leaves macro-F1 on the table: many windows are predicted `null` while their true
class is the runner-up. "Reclaiming" them (lowering a class threshold) trades precision for recall.
We model each class by real cache counts (TP,FP,FN) plus its reclaim capacity `k` (windows predicted
null with this class as runner-up) and reclaim precision `p` (milli: fraction of those truly this
class). Reclaiming `r` windows adds `g = p·r/1000` true positives and `r-g` false positives.

F1 PROFIT(c,r) = F1(after) − F1(before). We rank classes by best achievable profit, and use Plausible
to SEARCH reclaim allocations and exhibit a witness that recovers net macro-F1 (refuting "nothing helps").
Counts are exact Ints; F1 is milli-units (×1000). Reclaim precision p is the measured 0.11–0.20.
-/
namespace WearMissingF1

structure Cls where
  tp : Int
  fp : Int
  fn : Int
  k : Int
  p : Int       -- reclaim precision, milli
  name : String
deriving Repr

/-- milli-F1 = 1000 · 2TP/(2TP+FP+FN). -/
def f1m (tp fp fn : Int) : Int := if 2*tp+fp+fn ≤ 0 then 0 else (2000*tp) / (2*tp+fp+fn)
def base (c : Cls) : Int := f1m c.tp c.fp c.fn
/-- F1 after reclaiming r windows: g=p·r/1000 true (TP↑, FN↓), r−g false (FP↑). -/
def f1At (c : Cls) (r : Int) : Int := let g := c.p*r/1000; f1m (c.tp+g) (c.fp+(r-g)) (c.fn-g)
def profitAt (c : Cls) (r : Int) : Int := f1At c r - base c
/-- Candidate reclaim levels: 0,10%,…,100% of capacity. -/
def grid (c : Cls) : List Int := (List.range 11).map (fun (i:Nat) => c.k * (Int.ofNat i) / 10)
def bestProfit (c : Cls) : Int := (grid c).foldl (fun m r => max m (profitAt c r)) 0
def bestR (c : Cls) : Int := (grid c).foldl (fun br r => if profitAt c r > profitAt c br then r else br) 0

/-- Real per-class cache numbers (LOSO inertial). (TP,FP,FN, reclaim-cap k, reclaim-precision p‰). -/
def CLS : List Cls := [
  ⟨9563,3812,3293,948,92,"jog"⟩, ⟨5812,4601,5016,2204,185,"jogR"⟩, ⟨8919,1976,2217,2479,109,"jogSk"⟩,
  ⟨9967,2047,2785,4029,191,"jogSi"⟩, ⟨8540,1311,2296,3258,108,"jogB"⟩, ⟨3535,2714,8349,19425,199,"strT"⟩,
  ⟨3908,4225,8540,31416,142,"strL"⟩, ⟨562,1335,10766,25837,111,"strSh"⟩, ⟨3961,5331,7203,16210,168,"strH"⟩,
  ⟨6296,3862,5232,8787,178,"strLu"⟩, ⟨4218,4442,6354,6605,196,"pu"⟩, ⟨4082,3980,7430,7192,158,"puC"⟩,
  ⟨4241,4485,7531,10595,138,"su"⟩, ⟨5191,3734,6693,12483,182,"suC"⟩, ⟨6465,4676,5087,9943,172,"burp"⟩,
  ⟨4433,3488,7707,16543,111,"lun"⟩, ⟨4973,4834,7151,9646,158,"lunC"⟩, ⟨4329,4047,6115,7029,167,"bench"⟩ ]
def NULLc : Cls := ⟨126931,67698,22833,0,0,"null"⟩

/-- RERANK BY F1 PROFIT: each class's (name, gross milli-F1 profit, optimal reclaim r). Sorted desc. -/
def ranking : List (String × Int × Int) :=
  ((CLS.map (fun c => (c.name, bestProfit c, bestR c))).toArray.qsort
    (fun a b => decide (a.2.1 > b.2.1))).toList

#eval ranking
/- gross total recoverable (sum of per-class profits, ÷19 for macro pts) -/
#eval (CLS.map bestProfit).foldl (·+·) 0
/- null TAX: applying all best reclaims, total true-null windows lost from null = Σ (1000-p)·r/1000 -/
#eval (CLS.map (fun c => let r := bestR c; (1000-c.p)*r/1000)).foldl (·+·) 0
#eval (CLS.map (fun c => let r := bestR c; c.p*r/1000)).foldl (·+·) 0   -- null FP removed (truly-c)

/-- NET macro after applying each class's best reclaim AND charging the null tax. -/
def netMacro : Int :=
  let lostNullTP := (CLS.map (fun c => let r := bestR c; (1000-c.p)*r/1000)).foldl (·+·) 0
  let remNullFP  := (CLS.map (fun c => let r := bestR c; c.p*r/1000)).foldl (·+·) 0
  let nullNew := f1m (NULLc.tp - lostNullTP) (NULLc.fp - remNullFP) (NULLc.fn + lostNullTP)
  let clsNew  := (CLS.map (fun c => f1At c (bestR c))).foldl (·+·) 0
  (clsNew + nullNew) / 19
#eval base NULLc        -- null milli-F1 before
#eval netMacro          -- macro ×1000 AFTER profit-maximizing reclaim (vs baseline 525)

/-! ## Plausible: search reclaim allocations and exhibit the missing-F1 witness.
Allocation = per-class reclaim fraction in tenths (Fin 11 each). Refuting "every allocation loses or
ties baseline" forces Plausible to hand back a concrete allocation that PROFITS — the missing F1. -/
def macroOf (fr : List Int) : Int :=        -- fr_i in 0..10 (tenths of capacity)
  let rs := (CLS.zip fr).map (fun (c,f) => c.k * f / 10)
  let lostNullTP := ((CLS.zip rs).map (fun (c,r) => (1000-c.p)*r/1000)).foldl (·+·) 0
  let remNullFP  := ((CLS.zip rs).map (fun (c,r) => c.p*r/1000)).foldl (·+·) 0
  let nullNew := f1m (NULLc.tp - lostNullTP) (NULLc.fp - remNullFP) (NULLc.fn + lostNullTP)
  let clsNew  := ((CLS.zip rs).map (fun (c,r) => f1At c r)).foldl (·+·) 0
  (clsNew + nullNew) / 19

/- all-50%-reclaim allocation vs baseline 525 -/
#eval macroOf (List.replicate 18 5)
/- Plausible searches tenths-allocations for one beating baseline (refute -> witness). -/
example : ∀ fr : List (Fin 11), fr.length = 18 → macroOf (fr.map (·.val)) < 540 := by plausible

end WearMissingF1
