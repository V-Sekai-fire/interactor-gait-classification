"""Extract named, unit-known gait features from AddBiomechanics .b3d files.

Each .b3d (SubjectOnDisk) holds N trials. We compute one feature row per trial
(restricted to frames with valid GRF). Features have documented units so they can
be cross-referenced against the anonymous 321-column gait_features.parquet schema.

DOF index -> coordinate (23 dynamic DOFs; the two knee_*_beta couplers are dropped):
  0 pelvis_tilt 1 pelvis_list 2 pelvis_rotation 3 pelvis_tx 4 pelvis_ty 5 pelvis_tz
  6 hip_flexion_r 7 hip_adduction_r 8 hip_rotation_r 9 knee_angle_r 10 ankle_angle_r
  11 subtalar_r 12 mtp_r 13 hip_flexion_l 14 hip_adduction_l 15 hip_rotation_l
  16 knee_angle_l 17 ankle_angle_l 18 subtalar_l 19 mtp_l
  20 lumbar_extension 21 lumbar_bending 22 lumbar_rotation
"""
import numpy as np
import nimblephysics as nimble

DOF = {  # name -> index in the 23-long pos/vel/tau vectors
    'hip_flex_r':6,'hip_add_r':7,'hip_rot_r':8,'knee_r':9,'ankle_r':10,
    'hip_flex_l':13,'hip_add_l':14,'hip_rot_l':15,'knee_l':16,'ankle_l':17,
    'pelvis_tilt':0,'pelvis_list':1,'pelvis_rot':2,
}
R2D = 180.0/np.pi


def _heelstrikes(vgrf, dt, thresh):
    """Indices where vertical GRF rises through `thresh` (foot contact onset)."""
    above = vgrf > thresh
    on = np.where((~above[:-1]) & (above[1:]))[0] + 1
    return on


_NM = nimble.biomechanics.MissingGRFReason.notMissingGRF


def _activity(name):
    n = name.lower()
    for k in ('gait', 'walk', 'run', 'tread', 'sts', 'sit', 'stair', 'jump',
              'squat', 'static', 'cal', 'dj', 'cmj', 'land'):
        if k in n:
            return k
    return 'other'


def trial_features(sub, t):
    L = sub.getTrialLength(t)
    if L < 30:
        return None
    dt = sub.getTrialTimestep(t)
    mass = sub.getMassKg(); height = sub.getHeightM(); bw = mass * 9.81
    frames = sub.readFrames(t, 0, L, includeSensorData=False, includeProcessingPasses=True)
    pp = [f.processingPasses[-1] for f in frames]
    pos = np.array([p.pos for p in pp])          # (L,23) rad / m
    vel = np.array([p.vel for p in pp])          # (L,23)
    grf = np.array([p.groundContactForce for p in pp])  # (L,9): 3 contacts x xyz
    com_vel = np.array([p.comVel for p in pp])   # (L,3) m/s
    good = np.array([m == _NM for m in sub.getMissingGRF(t)[:L]], dtype=bool)

    f = {'activity': _activity(sub.getTrialName(t)), 'n_frames': int(L),
         'n_good_grf': int(good.sum()), 'duration_s': L * dt}

    # --- kinematic features: computed on ALL frames (no GRF needed) ---
    for name, idx in DOF.items():
        ang = pos[:, idx] * R2D
        f[f'{name}_rom_deg'] = float(ang.max() - ang.min())
        f[f'{name}_mean_deg'] = float(ang.mean())
        f[f'{name}_peak_vel_dps'] = float(np.abs(vel[:, idx] * R2D).max())
    f['walking_speed_mps'] = float(np.linalg.norm(com_vel[:, [0, 2]], axis=1).mean())
    f['speed_norm'] = f['walking_speed_mps'] / np.sqrt(9.81 * height)

    # --- GRF / timing features: only where GRF is valid ---
    if good.sum() >= 30:
        vgrf = grf[:, 1::3].sum(axis=1)            # vertical = y-comp of contacts
        f['peak_vgrf_bw'] = float(np.nanmax(vgrf[good]) / bw)
        f['mean_vgrf_bw'] = float(np.nanmean(vgrf[good]) / bw)
        f['stance_fraction'] = float((vgrf[good] > 0.05 * bw).mean())
        hs = _heelstrikes(vgrf, dt, 0.1 * bw)
        stride_t = np.diff(hs) * dt if len(hs) >= 3 else np.array([])
        stride_t = stride_t[(stride_t > 0.5) & (stride_t < 2.5)]
        if len(stride_t):
            f['stride_time_s'] = float(stride_t.mean())
            f['cadence_steps_min'] = float(120.0 / stride_t.mean())
            f['stride_length_m'] = float(f['walking_speed_mps'] * stride_t.mean())
    return f


def subject_rows(path, max_trials=None):
    sub = nimble.biomechanics.SubjectOnDisk(path)
    rows = []
    nt = sub.getNumTrials()
    for t in range(nt if max_trials is None else min(nt, max_trials)):
        try:
            r = trial_features(sub, t)
        except Exception as e:
            import sys
            print(f"  ! {path.split('/')[-1]} trial {t}: {type(e).__name__}: {e}", file=sys.stderr)
            r = None
        if r:
            r['subject'] = path.split('/')[-1].replace('.b3d','')
            r['trial'] = sub.getTrialName(t)
            r['mass_kg'] = sub.getMassKg(); r['height_m'] = sub.getHeightM()
            try:
                r['sex'] = str(sub.getBiologicalSex())
            except Exception:
                r['sex'] = 'unknown'
            try:
                r['age_years'] = float(sub.getAgeYears())
            except Exception:
                r['age_years'] = 0.0
            rows.append(r)
    return rows


if __name__ == '__main__':
    import sys, json
    out = []
    for p in sys.argv[1:]:
        out += subject_rows(p)
    import pandas as pd
    df = pd.DataFrame(out)
    df.to_parquet('/tmp/biomech_features.parquet', index=False)
    print(df.describe().T.to_string())
    print('\nrows:', len(df), 'cols:', df.shape[1])
