import numpy as np
import torch
import torch.nn as nn
from sklearn.preprocessing import MinMaxScaler

# LTP values
ltp = np.array([
    960.44, 892.88, 882.94, 895.22, 865.81,
    864.39, 856.64, 867.38, 877.59, 870.61,
    859.65, 850.54, 861.88, 848.50, 849.53,
    845.49, 842.19, 831.35, 826.49, 826.84
]).reshape(-1, 1)

# Normalize
scaler = MinMaxScaler()
ltp_scaled = scaler.fit_transform(ltp)

# Create sequences
def create_seq(data, seq_len=5):
    X, y = [], []
    for i in range(len(data) - seq_len):
        X.append(data[i:i+seq_len])
        y.append(data[i+seq_len])
    return torch.tensor(X, dtype=torch.float32), torch.tensor(y, dtype=torch.float32)

X, y = create_seq(ltp_scaled)

# LSTM model
class LSTM(nn.Module):
    def __init__(self): super().__init__()
    self.lstm = nn.LSTM(1, 32, batch_first=True)
    self.fc = nn.Linear(32, 1)
    def forward(self, x): return self.fc(self.lstm(x)[0][:, -1, :])

model = LSTM()
opt = torch.optim.Adam(model.parameters(), lr=0.01)
loss_fn = nn.MSELoss()

# Train
for _ in range(200):
    out = model(X)
    loss = loss_fn(out, y)
    opt.zero_grad()
    loss.backward()
    opt.step()

# Predict next 5
seq = torch.tensor(ltp_scaled[-5:], dtype=torch.float32).unsqueeze(0)
preds = []
for _ in range(5):
    with torch.no_grad():
        p = model(seq).item()
        preds.append(p)
        seq = torch.cat([seq[:, 1:, :], torch.tensor([[[p]]])], dim=1)

# Inverse scale
preds = scaler.inverse_transform(np.array(preds).reshape(-1, 1))
print("Next 5 LTP predictions:")
print(preds.flatten())
