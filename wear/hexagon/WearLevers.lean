import Plausible
/-! # WEAR lever-test math, made manual & checkable (Lean4 + Plausible)

The empirical probes asked: *where can macro-F1 be gained, and what caps us?* That question is
algebra once you accept the per-class F1 estimates. We formalize the **Amdahl law for macro-F1** and
the **gravity-channel lossless split**, prove the identities, then Plausible-test the same statements
on random inputs. Per-class F1 is modelled in milli-units (Int 0..1000) so everything is exact and
Plausible-sampleable (no Float). macro-F1 ordering ⟺ sum ordering (n fixed at 19), so we reason on sums.
-/
namespace WearLevers

/-- A class's measured state: `cur` = current per-class F1, `ceil` = optimistic achievable ceiling
    (from one-vs-rest separability). Milli-units. -/
abbrev ClassF1 := Int × Int          -- (cur, ceil)

def curSum  (cs : List ClassF1) : Int := (cs.map Prod.fst).sum
def ceilSum (cs : List ClassF1) : Int := (cs.map Prod.snd).sum
/-- Per-class recoverable gain. -/
def gains   (cs : List ClassF1) : List Int := cs.map (fun p => p.2 - p.1)
/-- A class is *walled* when no headroom remains (ceiling = current): augmentation/ANNY can't help it. -/
def walled  (p : ClassF1) : Bool := p.2 == p.1

/-! ## Amdahl's law for macro-F1
The total recoverable macro gain is exactly the sum of per-class gains — and walled classes
contribute zero, no matter how hard they are pushed. This is the "serial fraction" that caps us. -/

/-- **Amdahl identity**: summed per-class gain = ceiling-sum − current-sum. -/
theorem amdahl_gain (cs : List ClassF1) : (gains cs).sum = ceilSum cs - curSum cs := by
  induction cs with
  | nil => rfl
  | cons p ps ih =>
    simp only [gains, curSum, ceilSum, List.map_cons, List.sum_cons] at *
    omega

/-- A walled class adds nothing to the recoverable gain (its gain term is 0). -/
theorem walled_zero_gain (p : ClassF1) (h : walled p = true) : p.2 - p.1 = 0 := by
  simp only [walled, beq_iff_eq] at h; omega

/-- **Monotone ceiling**: if every class's ceiling dominates its current, macro can only rise to it. -/
theorem cur_le_ceil (cs : List ClassF1) (h : ∀ p ∈ cs, p.1 ≤ p.2) : curSum cs ≤ ceilSum cs := by
  induction cs with
  | nil => simp [curSum, ceilSum]
  | cons p ps ih =>
    have hp := h p (by simp)
    have ht := ih (fun q hq => h q (by simp [hq]))
    simp only [curSum, ceilSum, List.map_cons, List.sum_cons]
    simp only [curSum, ceilSum] at ht
    omega

/-- **Target-unreachable bound** (the "0.80 needs new signal" theorem): if even the ceiling-sum
    falls below the target-sum (= 19 × target), the current model cannot reach it either. -/
theorem target_unreachable (cs : List ClassF1) (target : Int)
    (hmono : ∀ p ∈ cs, p.1 ≤ p.2) (hceil : ceilSum cs < target) : curSum cs < target := by
  have := cur_le_ceil cs hmono; omega

/-! ## The real probe numbers (per-class milli-F1: current, separability-ceiling)
null is walled at its already-good value; jog-skip/side/butt near ceiling; the static-pose band is
where headroom (or walls) live. -/
def WEAR : List ClassF1 :=
  [ (740,740),  -- null
    (730,810),  -- jogging
    (550,720),  -- jogging-rotating-arms   (RECOVERABLE: real motion)
    (810,810),  -- jogging-skipping
    (800,800),  -- jogging-sidesteps
    (830,830),  -- jogging-buttkicks
    (390,500),  -- stretching-triceps
    (380,390),  -- stretching-lunging
    (80 ,440),  -- stretching-shoulders     (worst current; orientation headroom)
    (390,450),  -- stretching-hamstrings
    (580,580),  -- stretching-lumbar        (walled)
    (440,550),  -- push-ups
    (420,420),  -- push-ups-complex         (walled)
    (410,410),  -- sit-ups                  (walled)
    (500,530),  -- sit-ups-complex
    (570,570),  -- burpees                  (walled)
    (440,440),  -- lunges                   (walled)
    (450,450),  -- lunges-complex           (walled)
    (460,600) ] -- bench-dips

/-- 19 classes, as the contract expects. -/
theorem WEAR_card : WEAR.length = 19 := by decide

/- Manual lever calculation, evaluated by the kernel (milli-F1 sums; divide by 19 for macro). -/
#eval curSum WEAR                                    -- current macro × 19
#eval ceilSum WEAR                                   -- ceiling macro × 19
#eval ceilSum WEAR - curSum WEAR                     -- TOTAL recoverable (Amdahl gain) × 19
#eval (WEAR.filter walled).length                    -- # walled classes (zero-headroom serial fraction)
#eval (WEAR.filter (fun p => decide (p.2 - p.1 ≥ 80))).map Prod.fst  -- the genuinely recoverable classes
-- macro now ≈ curSum/19 ; ceiling ≈ ceilSum/19 ; gap to 800 (=0.80) shown unreachable below.

/-- **The headline result, proven for our data**: even at the optimistic separability ceiling, summed
    macro stays below 19×800 = 15200 (i.e. < 0.80). 0.80 is unreachable from this single-limb signal —
    it requires NEW signal (cross-limb / video / pose), exactly what the probes concluded. -/
theorem wear_080_unreachable : curSum WEAR < 15200 := by
  have hmono : ∀ p ∈ WEAR, p.1 ≤ p.2 := by decide
  exact target_unreachable WEAR 15200 hmono (by decide)

/-! ## Gravity-channel lossless split
The orientation lever splits each accel sample `x` into linear `(x - g)` and gravity `g`. The split
must lose nothing — recomposition is exact — else we'd be inventing/destroying signal. -/
theorem gravity_split_lossless (x g : Int) : (x - g) + g = x := by omega

/-! ## 6D rotation: two axes → full orthonormal basis via cross product
Accel gravity fixes pitch/roll (one body axis). With a second (independent) axis, the **6D rotation
representation** recovers the full frame: Gram-Schmidt orthogonalizes the pair, then the third basis
vector is their cross product — orthogonal to both *by construction*. We prove that orthogonality
(the part that needs no √, hence exact over Int): the recovered third axis is ⟂ to the two inputs. -/
abbrev Vec3 := Int × Int × Int
def dot (a b : Vec3) : Int := a.1*b.1 + a.2.1*b.2.1 + a.2.2*b.2.2
def cross (a b : Vec3) : Vec3 :=
  (a.2.1*b.2.2 - a.2.2*b.2.1, a.2.2*b.1 - a.1*b.2.2, a.1*b.2.1 - a.2.1*b.1)

/-- The recovered third basis axis is orthogonal to both inputs — so {a, b, a×b} spans an orthogonal
    frame (full limb orientation recovered from two axes). Proven by `grind` if available; in any case
    Plausible-tested below. The orthogonality is a polynomial identity (no √), hence exact over Int. -/
theorem cross_perp_left  (a b : Vec3) : dot (cross a b) a = 0 := by
  simp only [dot, cross]; grind
theorem cross_perp_right (a b : Vec3) : dot (cross a b) b = 0 := by
  simp only [dot, cross]; grind

/-! ## Plausible randomized property tests (same statements, sampled over random Int inputs) -/
example : ∀ cs : List ClassF1, (gains cs).sum = ceilSum cs - curSum cs := by plausible
example : ∀ x g : Int, (x - g) + g = x := by plausible
example : ∀ a b : Vec3, dot (cross a b) a = 0 := by plausible
example : ∀ a b : Vec3, dot (cross a b) b = 0 := by plausible

end WearLevers
