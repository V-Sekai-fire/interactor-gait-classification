"""Full-data 1D-CNN on raw 50x3 WEAR windows.
(1) held-out eval (subjects 16-19) for the honest macro-F1, (2) train on ALL train subjects ->
predict test -> submission. Labels encoded directly with the competition LABEL_MAP so the CNN's
class index IS target_feature. Raw NaNs (sensor dropouts) sanitized.
"""
import numpy as np, torch, torch.nn as nn, time
from sklearn.metrics import f1_score, accuracy_score

LABEL_MAP = {'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,
 'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,
 'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,
 'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}
NCLS = 19; DEV = "cuda"

d = np.load("wear_raw.npz", allow_pickle=True)
X = np.nan_to_num(d["X"].astype(np.float32)); g = d["g"]
y = np.array([LABEL_MAP[str(l)] for l in d["y"]], dtype=np.int64)


class CNN(nn.Module):
    def __init__(s):
        super().__init__(); s.net = nn.Sequential(
            nn.Conv1d(3,64,7,padding=3), nn.BatchNorm1d(64), nn.ReLU(), nn.MaxPool1d(2),
            nn.Conv1d(64,128,5,padding=2), nn.BatchNorm1d(128), nn.ReLU(), nn.MaxPool1d(2),
            nn.Conv1d(128,256,3,padding=1), nn.BatchNorm1d(256), nn.ReLU(),
            nn.Conv1d(256,256,3,padding=1), nn.BatchNorm1d(256), nn.ReLU(),
            nn.AdaptiveAvgPool1d(1), nn.Flatten(), nn.Dropout(0.4), nn.Linear(256, NCLS))
    def forward(s, x): return s.net(x)


def train(Xtr, ytr, epochs=100):
    mu = Xtr.reshape(-1,3).mean(0); sd = Xtr.reshape(-1,3).std(0)+1e-6
    Xn = np.nan_to_num((Xtr-mu)/sd).transpose(0,2,1)
    xt = torch.tensor(Xn, device=DEV); yt = torch.tensor(ytr, device=DEV)
    m = CNN().to(DEV); opt = torch.optim.AdamW(m.parameters(), 1e-3, weight_decay=1e-4)
    sch = torch.optim.lr_scheduler.CosineAnnealingLR(opt, epochs); lf = nn.CrossEntropyLoss(label_smoothing=0.05)
    t = time.time()
    for ep in range(epochs):
        m.train(); perm = torch.randperm(len(xt), device=DEV)
        for i in range(0, len(xt), 512):
            b = perm[i:i+512]; opt.zero_grad(); lf(m(xt[b]), yt[b]).backward(); opt.step()
        sch.step()
        if ep % 25 == 0: print(f"  ep{ep} loss={lf(m(xt[:2048]),yt[:2048]).item():.3f}", flush=True)
    print(f"  trained {epochs} ep in {time.time()-t:.0f}s", flush=True)
    return m, mu, sd


def predict(m, mu, sd, Xin):
    Xn = np.nan_to_num((np.nan_to_num(Xin.astype(np.float32))-mu)/sd).transpose(0,2,1)
    m.eval(); out=[]
    with torch.no_grad():
        for i in range(0, len(Xn), 4096):
            out.append(m(torch.tensor(Xn[i:i+4096], device=DEV)).argmax(1).cpu().numpy())
    return np.concatenate(out)


# (1) held-out eval
HO = {16,17,18,19}; te = np.isin(g, list(HO)); tr = ~te
print(f"=== held-out eval: train {tr.sum()} / holdout {te.sum()} ===", flush=True)
m, mu, sd = train(X[tr], y[tr])
p = predict(m, mu, sd, X[te])
f1 = f1_score(y[te], p, average="macro")
print(f"=== 1D-CNN HELD-OUT macro-F1 (subj 16-19) = {f1:.4f}  (TabM held-out 0.51) ===", flush=True)

# (2) full-data model -> test submission
print("=== full-data train -> submission ===", flush=True)
mf, muf, sdf = train(X, y)
torch.save(mf.state_dict(), "models_cnn.pt")
import pandas as pd
ti = np.load("test/test_inertial_data.npy", allow_pickle=True).astype(np.float32)
pred = predict(mf, muf, sdf, ti)
ss = pd.read_csv("sample_submission.csv"); ss["target_feature"] = pred.astype(int)
ss.to_csv("submission_cnn.csv", index=False)
print("wrote submission_cnn.csv | dist:", dict(sorted(pd.Series(pred).value_counts().items())), flush=True)
