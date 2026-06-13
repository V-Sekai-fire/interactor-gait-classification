"""Build a resumable Parquet feature cache over the ENTIRE AddBiomechanics train split.

For each addb_dataset_publication-*.zip:
  - list .b3d members under .../train/...
  - extract each member individually to a temp file, run feature extraction, delete it
  - write one shard parquet per zip: cache/<zipstem>.parquet  (skipped if it exists -> resumable)
Progress is appended to cache/progress.log so a monitor can tail it.
"""
import os, sys, glob, zipfile, tempfile, traceback, time
import pandas as pd
from extract_gait_features import subject_rows

ZIP_DIR = "/run/media/ernest.lee/Bulk/motion_model"
CACHE = "/chibifire-assets-2026w24/files/gait_classification/cache"
os.makedirs(CACHE, exist_ok=True)
LOG = os.path.join(CACHE, "progress.log")


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(LOG, "a") as fh:
        fh.write(line + "\n")


def process_zip(zp):
    stem = os.path.splitext(os.path.basename(zp))[0]
    shard = os.path.join(CACHE, stem + ".parquet")
    if os.path.exists(shard):
        return  # resumable: already done
    if os.path.getsize(zp) == 0:
        log(f"SKIP {stem}: zero-byte"); return
    rows = []
    try:
        with zipfile.ZipFile(zp) as zf:
            members = [m for m in zf.namelist() if m.endswith(".b3d") and "/train/" in m]
            log(f"{stem}: {len(members)} b3d members")
            for m in members:
                with tempfile.NamedTemporaryFile(suffix=".b3d", delete=False) as tf:
                    tmp = tf.name
                    with zf.open(m) as src:
                        while True:
                            chunk = src.read(1 << 24)
                            if not chunk:
                                break
                            tf.write(chunk)
                try:
                    r = subject_rows(tmp)
                    for row in r:
                        row["dataset"] = m.split("/train/")[1].split("/")[1]
                        row["member"] = m
                    rows += r
                except Exception as e:
                    log(f"  ! {m}: {type(e).__name__}: {e}")
                finally:
                    os.unlink(tmp)
    except zipfile.BadZipFile:
        log(f"SKIP {stem}: bad/incomplete zip"); return
    df = pd.DataFrame(rows)
    df.to_parquet(shard, index=False)
    log(f"DONE {stem}: {len(df)} trial-rows -> {os.path.basename(shard)}")


def main():
    zips = sorted(glob.glob(os.path.join(ZIP_DIR, "addb_dataset_publication-*.zip")))
    # also the standalone subject .b3d files (p1..p10, s3) sitting next to the zips
    standalone = sorted(glob.glob(os.path.join(ZIP_DIR, "*.b3d")))
    log(f"=== START: {len(zips)} zips + {len(standalone)} standalone b3d ===")
    for zp in zips:
        process_zip(zp)
    # standalone files -> one shard each
    for sp in standalone:
        stem = "standalone_" + os.path.splitext(os.path.basename(sp))[0]
        shard = os.path.join(CACHE, stem + ".parquet")
        if os.path.exists(shard):
            continue
        try:
            rows = subject_rows(sp)
            for row in rows:
                row["dataset"] = "standalone"; row["member"] = os.path.basename(sp)
            pd.DataFrame(rows).to_parquet(shard, index=False)
            log(f"DONE {stem}: {len(rows)} rows")
        except Exception as e:
            log(f"  ! {sp}: {type(e).__name__}: {e}")
    # combine
    shards = sorted(glob.glob(os.path.join(CACHE, "*.parquet")))
    shards = [s for s in shards if os.path.basename(s) != "biomech_features.parquet"]
    allrows = pd.concat([pd.read_parquet(s) for s in shards if os.path.getsize(s) > 0], ignore_index=True)
    out = os.path.join(CACHE, "biomech_features.parquet")
    allrows.to_parquet(out, index=False)
    log(f"=== COMBINED: {len(allrows)} rows from {len(shards)} shards -> {out} ===")


if __name__ == "__main__":
    main()
