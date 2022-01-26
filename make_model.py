import pandas as pd
import numpy as np
import torch
from torch import nn, optim
from net import Net

waza_list = ["hadouken", "hiziuti", "left_punch", "right_punch", "left_kick", "right_kick", "sakotuwari", "syoryuken", "no"]

#csvデータのロード
df1 = pd.read_csv('./csv/data1.csv', index_col=0)
df2 = pd.read_csv('./csv/data2.csv', index_col=0)

#yデータの取得
label = []
label.append(df1["label"].values)
label.append(df2["label"].values)
label = np.concatenate(label, axis=0)
y = np.zeros([len(label), len(waza_list)])
for i, label_num in enumerate(label):
    y[i, label_num] = 1

#xデータの取得
df1 = df1.drop(columns='label')
df2 = df2.drop(columns='label')
x1 = df1.values
x2 = df2.values
x = np.vstack([x1, x2])
input_dim = x.shape[1]

#テンソルに変換
x = torch.from_numpy(x).float()
y = torch.from_numpy(y).float()

#dataloaderの作成
batch_size = 256
dataset = torch.utils.data.TensorDataset(x, y)
train_dataloader = torch.utils.data.DataLoader(dataset, batch_size, shuffle=True)

#学習
max_epoch = 50
criterion = nn.MSELoss()
device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)
model = Net(input_dim=input_dim, hidden_dim=255, n_layers=3).to(device)
optimizer = optim.Adam(model.parameters(), lr = 0.0033)

model.train()
for epoch in range(max_epoch):
    for batch in train_dataloader:
        x, t = batch
        x = x.to(device)
        t = t.to(device)
        optimizer.zero_grad()
        y = model(x)
        loss = criterion(y, t)
        loss.backward()
        optimizer.step()

#学習済みモデルの保存
torch.save(model.state_dict(), "./model/waza_model.pth")