# Real-Street-Fighter

## 概要
こちらの動きに合わせて格闘ゲーム内のキャラが動いたり、技を出すシステムを作成した。<br>
プレイヤーは技を出すために予め決められた動作を行い、その動きをカメラで撮影する。<br>
プログラムは撮影した動きが何の技を繰り出しているかをリアルタイムで識別し、ゲーム内にその技のコマンドを送ることで技が出る流れとなっている。<br>
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
| 昇竜拳 | 左右どちらかの腕を下から上に振り上げる |

#### キャラの移動
技以外にも、体を左や右にスライドさせたり、ジャンプの動作をすることで左移動、右移動、ジャンプを行うことができる。<br>


https://user-images.githubusercontent.com/52659785/151190388-09125503-ad9d-4955-906a-a509ed72d590.mp4


<br>

## 詳細
#### pytorch-openposeを利用した骨格点検出
本システムはカメラに映った人物の骨格点データを入力とし、深層学習を用いて技の識別を行っている。<br>
骨格点データを得るために、OpenPoseという、人物の骨格を深層学習で推定するシステムを使用した。<br>

![51 (3)](https://user-images.githubusercontent.com/52659785/153494938-ae5e99ea-b04c-4702-aa9b-1f9f145cc0bc.png)

pytorch-openposeは、OpenPoseをPytorchで動かせるようにしたものであり、詳細は以下を参照。

https://github.com/Hzzone/pytorch-openpose

#### 骨格店座標の2点間の角度データへの変換
骨格点データを入力にすると書いたが、これは座標データであるため、このままでは被写体の体格や映る位置によって値が変わってしまい、識別精度に影響を及ぼす可能性が高くなる。<br>
そこで、全18個の骨格点データにおいて、首の座標を原点としたときの、その他17個の骨格点との2点間の角度をそれぞれ求め、それらを入力とすることで、被写体による影響を軽減することに成功した。

![画像4](https://user-images.githubusercontent.com/52659785/155222701-2ac76e96-8ff7-4b5b-9610-8b273da8b759.png)


#### ディープラーニングを用いた技識別モデルの作成
技の識別を行うモデルは、約6000枚の画像から得られる骨格点データを角度データに変換したものを元にPytorchを用いて作成した。<br>
学習率や層の数などのパラメータの決定には、Optunaと呼ばれるハイパーパラメータ自動最適化フレームワークを用いた。<br>
`net.py`と`make_model.py`にそれぞれニューラルネットワークの構造とモデルを作成するプログラムが記述されているため、気になる方はそちらを参照。
