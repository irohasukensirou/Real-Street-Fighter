# Real-Street-Fighter

## 概要
こちらの動きに合わせてゲーム内のキャラが動いたり、技を出すシステムを作成した。<br>
プレイヤーはStreet Fighter Vという格闘ゲームにおける技の動きを再現して、それをカメラで撮影する。<br>
プログラムは、撮影した動きが何の技を繰り出しているかをリアルタイムで識別し、ゲーム内にその技のコマンドを送ることで技が出るという流れになっている。<br>
<br>
## デモ映像

https://user-images.githubusercontent.com/52659785/151023653-dfe616ad-49e3-4249-8e7b-31638bee4842.mp4

<br>

## 要件
#### 環境
Python 3.7上で動くことを想定。

#### ライブラリ
必要なライブラリは`requirements.txt`に記載している。<br>
pipコマンドでまとめて取り込める。
```
pip install -r requirements.txt
```
また、以下のサイトから自身の環境に合わせてPytorchライブラリをインストールする。

https://pytorch.org
#### 機材
- Webカメラ
- [Street Fighter V](https://store.steampowered.com/app/310950/Street_Fighter_V/)

#### モデルのダウンロード
以下のリンクから`body_pose_model.pth`をダウンロードし、`model`フォルダ内に入れる。

https://www.dropbox.com/sh/7xbup2qsn7vvjxo/AABWFksdlgOMXR_r5v3RwKRYa?dl=0

<br>

## 使い方
1. PCにカメラを繋ぎ、カメラに全身が写ることを確認する。
2. Street Fighter Vを起動し対戦を開始する(トレーニングモードでCPUと対戦することを推奨)。
3. `main.py`を実行し、以下に示す各技に求められる動作をすることでゲーム内で技が出る。
```
python main.py
```
#### 技の種類
| 技名 | 求められる動作 |
| --- | --- |
| 波動拳 | かめはめ波のように両手を合わせて前に突き出す |
| 肘打ち | 左右どちらかの肘を前に突き出す |
| 左パンチ | 左腕を前に突き出す |
| 右パンチ | 右腕を前に突き出す |
| 左キック | 左足を前に繰り出す |
| 右キック | 右足を前に繰り出す |
| 鎖骨割り | 左右どちらかの腕を上から下に振り下ろす |
| 昇竜拳 | 左右どちらかの腕をしたから上に振り上げる |
<br>

## 詳細
#### ディープラーニングによる技の識別
本システムは、カメラに映った人物の骨格点データを入力として、ディープラーニングを用いて技の識別を行っている。<br>
識別モデルは約6000枚の画像データを元にPytorchを用いて作成した。<br>
`net.py`と`make_model.py`にそれぞれニューラルネットワークの構造とモデルを作成するプログラムが記述されているため、気になる方はそちらを参照。

#### pytorch-openposeを利用した骨格点検出
カメラに映った人物から骨格点データを得るために、OpenPoseという、人物の骨格を深層学習で推定するシステムを使用した。<br>
pytorch-openposeは、OpenPoseをPytorchで動かせるようにしたものであり、詳細は以下を参照。

https://github.com/Hzzone/pytorch-openpose
