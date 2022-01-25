# street-fighter
Output the subject's movement as a technique in the game.

## 概要
こちらの動きに合わせてゲーム内のキャラが動いたり、技を出すシステムを作った。<br>
プレイヤーはStreet Fighter Vという格闘ゲームにおける技の動きを真似て、それをカメラでリアルタイムで撮影する。<br>
プログラムは、撮影したものが何の技を繰り出しているかを自動で識別し、ゲーム内にその技のコマンドを送ることで技が出るという流れになっている。<br>

## 要件
#### 環境
Python 3.7上で動くことを想定。

#### ライブラリ
必要なライブラリはアップしたテキストファイルに記載している。<br>
pipコマンドでまとめて取り込める。
```
pip install -r requirements.txt
```
#### 機材
- Webカメラ
- Street Fighter V(Steamで購入できる)

#### モデルのダウンロード
以下のリンクから`body_pose_model.pht`をダウンロードし、`model`フォルダ内に入れる。

https://www.dropbox.com/sh/7xbup2qsn7vvjxo/AABWFksdlgOMXR_r5v3RwKRYa?dl=0

## 使い方
PCにカメラを繋ぎ、Street Fighter Vを起動し対戦を開始する(トレーニングモードでCPUと対戦することを推奨)。<br>
`main.py`を実行し、カメラに全身が写るようにし、ゲーム内の技の動きを真似ることで
```
python main.py
```
#### 技の種類


## 詳細
#### ディープラーニングによる技の識別
本システムは、カメラに映った人物の骨格点データを入力として、ディープラーニングを用いて技の識別を行っている。<br>
識別モデルは約6000枚の画像データを元にPytorchを用いて作成した。<br>
`net.py`と`make_model.py`にそれぞれニューラルネットワークの構造とモデルを作成するプログラムが記述されているため、気になる方はそちらを参照。

#### pytorch-openposeを利用した骨格点検出
カメラに映った人物から骨格点データを得るために、OpenPoseという、人物の骨格を深層学習で推定するシステムを使用した。<br>
pytorch-openposeは、OpenPoseをPytorchで動かせるようにしたものであり、以下のリンクから利用することができる。

https://github.com/Hzzone/pytorch-openpose

