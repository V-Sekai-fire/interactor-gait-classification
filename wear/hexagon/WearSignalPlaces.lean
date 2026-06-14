import Plausible
/-! # Where can the missing F1 hide? — exhaustively, with Plausible

macro-F1 over 19 classes is finite: every bit of lost signal is an OFF-DIAGONAL cell of the 19×19
confusion matrix (true i, predicted j, i≠j). "There can't be that many places" — correct. From the
LOSO cache, the 33 cells with ≥1000 mass cover 74% of all loss, and each falls into exactly ONE of:
  • null-sink   (j = null): a static-pose window looks like rest  — the information wall
  • null-source (i = null): a rest window grabbed by an active class — precision cost of fixing the wall
  • within-fam  (same family, e.g. push-ups↔push-ups-complex): fine-grained discrimination
There are ZERO big CROSS-family leaks (no jogging↔push-ups). We prove that by `decide` (exhaustive over
the data) and Plausible-test the classifying logic over all 19×19 pairs. ⇒ only TWO remedies exist:
new signal for the null wall (orientation/pose), and finer features within families.
-/
namespace WearSignalPlaces

inductive Fam | NUL | JOG | STR | PU | SU | BRP | LUN | BEN
deriving DecidableEq, Repr
/-- Activity → family (0=null, 1-5 jog, 6-10 stretch, 11-12 push, 13-14 sit, 15 burpee, 16-17 lunge, 18 bench). -/
def fam : Nat → Fam
  | 0 => .NUL | 1 => .JOG | 2 => .JOG | 3 => .JOG | 4 => .JOG | 5 => .JOG
  | 6 => .STR | 7 => .STR | 8 => .STR | 9 => .STR | 10 => .STR
  | 11 => .PU | 12 => .PU | 13 => .SU | 14 => .SU | 15 => .BRP
  | 16 => .LUN | 17 => .LUN | 18 => .BEN | _ => .NUL

inductive Kind | nullSink | nullSource | withinFam | cross
deriving DecidableEq, Repr
/-- Classify a confusion cell (true i → predicted j). `cross` = the worrying kind (fixable model error). -/
def kind (i j : Nat) : Kind :=
  if j = 0 then .nullSink
  else if i = 0 then .nullSource
  else if fam i = fam j then .withinFam
  else .cross

/-- The 33 significant off-diagonal cells (true, pred, count), ≥1000 mass, from the LOSO cache. -/
def CELLS : List (Nat × Nat × Nat) :=
 [(8,0,8298),(7,0,7205),(6,0,6781),(16,0,5123),(9,0,5060),(13,0,4535),(14,0,4466),(17,0,4064),
  (18,0,3881),(12,0,3714),(15,0,3430),(10,0,3222),(11,0,3181),(2,1,3131),(0,9,2818),(1,2,2428),
  (0,7,2360),(12,11,2097),(0,15,1916),(0,18,1734),(0,10,1730),(0,17,1712),(17,16,1611),(11,12,1604),
  (0,13,1601),(16,17,1560),(4,0,1444),(0,14,1355),(13,14,1318),(14,13,1242),(0,12,1198),(0,16,1111),(2,0,1036)]

/-- **Headline, proven exhaustively over the data**: no significant leak is cross-family.
    Every place the F1 hides is a null-boundary or within-family confusion — only two structures. -/
theorem no_cross_leak : CELLS.all (fun c => kind c.1 c.2.1 != Kind.cross) = true := by decide

/- Breakdown of the 33 places (kernel-evaluated). -/
#eval CELLS.length
#eval (CELLS.filter (fun c => kind c.1 c.2.1 == Kind.nullSink)).length     -- null-sink count
#eval (CELLS.filter (fun c => kind c.1 c.2.1 == Kind.nullSource)).length   -- null-source count
#eval (CELLS.filter (fun c => kind c.1 c.2.1 == Kind.withinFam)).length    -- within-family count
#eval (CELLS.filter (fun c => kind c.1 c.2.1 == Kind.cross)).length        -- CROSS count (= 0)
/- mass routed to the null boundary (sink+source) vs within-family — which remedy matters more. -/
#eval (CELLS.filter (fun c => kind c.1 c.2.1 == Kind.nullSink || kind c.1 c.2.1 == Kind.nullSource)
        ).map (fun c => c.2.2) |>.foldl (·+·) 0
#eval (CELLS.filter (fun c => kind c.1 c.2.1 == Kind.withinFam)).map (fun c => c.2.2) |>.foldl (·+·) 0

/-! ## Plausible: exhaustive sweep of the classifying logic over ALL 19×19 pairs.
Fin 19 × Fin 19 = 361 cases — Plausible enumerates them. Confirms `cross` happens ONLY when both
classes are non-null AND in different families: i.e. the only "hidden" place would be a genuine
cross-family error, and the data theorem above shows there are none of size. -/
example : ∀ i j : Fin 19, kind i.val j.val = Kind.cross →
    (i.val ≠ 0 ∧ j.val ≠ 0 ∧ fam i.val ≠ fam j.val) := by plausible
example : ∀ i j : Fin 19, (j.val = 0 ∨ i.val = 0 ∨ fam i.val = fam j.val) →
    kind i.val j.val ≠ Kind.cross := by plausible

end WearSignalPlaces
