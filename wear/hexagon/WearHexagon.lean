import Plausible
/-! WEAR label-encoding contract (hexagon core).
    The competition target_feature is a fixed map from 19 activity classes to {0,…,18}.
    We model it as a total bijection and prove round-trip soundness; Plausible randomly
    property-tests the same contract. -/

namespace WearHexagon

/-- The 19 WEAR activity classes (order = paper/data-card order). -/
inductive Activity
  | null | jogging | joggingRotatingArms | joggingSkipping | joggingSidesteps
  | joggingButtKicks | stretchingTriceps | stretchingLunging | stretchingShoulders
  | stretchingHamstrings | stretchingLumbarRotation | pushUps | pushUpsComplex
  | sitUps | sitUpsComplex | burpees | lunges | lungesComplex | benchDips
deriving DecidableEq, Repr

open Activity

/-- The competition LABEL_MAP: Activity → target_feature code. -/
def encode : Activity → Nat
  | null => 0 | jogging => 1 | joggingRotatingArms => 2 | joggingSkipping => 3
  | joggingSidesteps => 4 | joggingButtKicks => 5 | stretchingTriceps => 6
  | stretchingLunging => 7 | stretchingShoulders => 8 | stretchingHamstrings => 9
  | stretchingLumbarRotation => 10 | pushUps => 11 | pushUpsComplex => 12
  | sitUps => 13 | sitUpsComplex => 14 | burpees => 15 | lunges => 16
  | lungesComplex => 17 | benchDips => 18

/-- Inverse decode (partial on Nat, total on the valid 0..18 range). -/
def decode : Nat → Option Activity
  | 0 => some null | 1 => some jogging | 2 => some joggingRotatingArms
  | 3 => some joggingSkipping | 4 => some joggingSidesteps | 5 => some joggingButtKicks
  | 6 => some stretchingTriceps | 7 => some stretchingLunging | 8 => some stretchingShoulders
  | 9 => some stretchingHamstrings | 10 => some stretchingLumbarRotation | 11 => some pushUps
  | 12 => some pushUpsComplex | 13 => some sitUps | 14 => some sitUpsComplex
  | 15 => some burpees | 16 => some lunges | 17 => some lungesComplex | 18 => some benchDips
  | _ => none

/-- Every activity is in range 0..18 (shape-honesty for the submission column). -/
theorem encode_lt_19 (a : Activity) : encode a < 19 := by cases a <;> decide

/-- Round-trip soundness: decoding an encoded label recovers it (no off-by-one / collision). -/
theorem decode_encode (a : Activity) : decode (encode a) = some a := by cases a <;> rfl

/-- Injectivity (no two classes share a code). -/
theorem encode_injective {a b : Activity} (h : encode a = encode b) : a = b := by
  cases a <;> cases b <;> simp_all [encode]

/-- Plausible property test (randomized): over the valid code range, decode∘encode round-trips
    and codes stay in 0..18 — the same contract the theorems prove, sampled. -/
example : ∀ i : Fin 19, (decode i.val).map encode = some i.val := by plausible

example : ∀ i : Fin 19, ∀ j : Fin 19, decode i.val = decode j.val → i.val = j.val ∨ decode i.val = none := by
  plausible

end WearHexagon
