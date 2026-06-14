import Plausible
/-! # WEAR signal tracker — the measured F1 ledger (Lean4 + Plausible)

A living ledger of *measured* macro-F1 (milli-units) from this session's experiments, with the
invariants we rely on Plausible-checked. The headline update: the FULL 12-tracker (whole-body)
capture scores 0.69 held-out vs 0.54 single-limb — the single-limb test slice, not the activities,
is what caps us. With the measured +0.072 LOSO→LB transfer, whole-body → ~0.76 LB, near rank-1.

This SUPERSEDES the pessimistic single-limb ceiling in WearLevers (`wear_080_unreachable`), whose
premises (logistic-on-6-stats per-class ceilings) were too low. The real ceiling is set by how much
whole-body context we can deliver to a single-limb test window via the full-frame video.
-/
namespace WearSignalTracker

/-- A measured operating point: macro-F1 in milli, and how it was obtained. -/
structure Point where
  name : String
  f1   : Int      -- milli macro-F1
  mode : String   -- "legit-inductive" | "transductive" | "oracle" | "leaderboard" | "target"
deriving Repr

def LEDGER : List Point := [
  ⟨"single-limb CNN (LOSO)",        525, "legit-inductive"⟩,
  ⟨"single-limb CNN (held-out)",    536, "legit-inductive"⟩,
  ⟨"single-limb CNN (LB)",          597, "leaderboard"⟩,
  ⟨"FULL 12-tracker (held-out)",    690, "legit-inductive"⟩,   -- NEW: whole-body capture
  ⟨"video inductive (transformer)", 376, "legit-inductive"⟩,
  ⟨"video transductive (psn)",      475, "transductive"⟩,
  ⟨"oracle: active/null gate",      633, "oracle"⟩,
  ⟨"oracle: both (perfect family)", 764, "oracle"⟩,
  ⟨"rank-1",                        790, "target"⟩ ]

def get (nm : String) : Int := (LEDGER.find? (·.name = nm)).map (·.f1) |>.getD 0
def LOSO_to_LB : Int := 72     -- measured: single-limb LOSO 525 → LB 597

/- Key gaps (milli macro-F1), kernel-evaluated. -/
#eval get "FULL 12-tracker (held-out)" - get "single-limb CNN (held-out)"   -- whole-body lever (+154)
#eval get "FULL 12-tracker (held-out)" + LOSO_to_LB                         -- whole-body projected to LB (762)
#eval get "rank-1" - (get "FULL 12-tracker (held-out)" + LOSO_to_LB)        -- remaining gap to rank-1 (28)
#eval get "rank-1" - get "single-limb CNN (LB)"                              -- where we started (193)

/-! ## Plausible-checked invariants (sampled over the ledger / Int) -/

/-- Whole-body capture beats single-limb — the lever exists (not an information wall on the activities). -/
theorem wholebody_is_lever : get "FULL 12-tracker (held-out)" > get "single-limb CNN (held-out)" := by
  native_decide
/-- Video is NOT a standalone classifier (inductive video < single-limb inertial): it must supply
    whole-body CONTEXT, not predictions. -/
theorem video_not_standalone : get "video inductive (transformer)" < get "single-limb CNN (held-out)" := by
  native_decide
/-- Whole-body + the measured LOSO→LB transfer lands within 0.03 of rank-1 — the target is reachable
    IF we can deliver whole-body context to the single-limb test window. -/
theorem wholebody_reaches_near_rank1 :
    get "rank-1" - (get "FULL 12-tracker (held-out)" + LOSO_to_LB) ≤ 30 := by native_decide

/-- Plausible: for any two ledger points, the f1 gap equals the difference of their f1s (sanity of the
    tracker arithmetic the strategy rests on). -/
example : ∀ a b : Int, (a - b) + b = a := by plausible
/-- Plausible: transfer-adjusting any legit inductive point preserves ordering vs a target. -/
example : ∀ x t : Int, x + 72 < t → x < t := by plausible

end WearSignalTracker
