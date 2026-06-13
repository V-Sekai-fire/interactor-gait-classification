"""Extract CLEAN joint kinematics (+ recorded sex) from raw .b3d for the caldata studies,
to test whether body MOTION (not body size) carries gender signal.
Reads /tmp/study_members.txt (zip<TAB>member), extracts each subject's b3d, runs
extract_gait_features.subject_rows (kinematic gait features + sex/age/mass/height).
"""
import os, sys, zipfile, tempfile
import pandas as pd
from extract_gait_features import subject_rows

ZIP_DIR = "/run/media/ernest.lee/Bulk/motion_model"
MAX_SUBJECTS = int(sys.argv[1]) if len(sys.argv) > 1 else 60
MAX_TRIALS = 8


def main():
    members = [l.strip().split("\t") for l in open("/tmp/study_members.txt") if "\t" in l]
    # dedupe by member path, cap
    seen = set(); picked = []
    for zp, m in members:
        if m in seen:
            continue
        seen.add(m); picked.append((zp, m))
        if len(picked) >= MAX_SUBJECTS:
            break
    print(f"extracting {len(picked)} subjects", flush=True)
    rows = []
    for i, (zp, m) in enumerate(picked):
        try:
            with zipfile.ZipFile(os.path.join(ZIP_DIR, zp)) as zf, \
                 tempfile.NamedTemporaryFile(suffix=".b3d", delete=False) as tf:
                tmp = tf.name
                with zf.open(m) as src:
                    while True:
                        b = src.read(1 << 24)
                        if not b:
                            break
                        tf.write(b)
            r = subject_rows(tmp, max_trials=MAX_TRIALS)
            study = m.split("/train/")[-1].split("/test/")[-1].split("/")[1] if "Formatted" not in m.split("/")[2] else m.split("/")[3]
            for row in r:
                row["study_member"] = m
            rows += r
            print(f"  [{i+1}/{len(picked)}] {m.split('/')[-1]}: {len(r)} rows", flush=True)
        except Exception as e:
            print(f"  ! {m}: {type(e).__name__}: {e}", flush=True)
        finally:
            try:
                os.unlink(tmp)
            except Exception:
                pass
    df = pd.DataFrame(rows)
    df.to_parquet("clean_kinematics.parquet", index=False)
    print(f"\nwrote clean_kinematics.parquet: {len(df)} rows, {df['subject'].nunique()} subjects, "
          f"sex={df['sex'].value_counts().to_dict()}")


if __name__ == "__main__":
    main()
