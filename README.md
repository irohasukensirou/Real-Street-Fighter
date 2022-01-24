# street-fighter
Output the subject's movement as a technique in the game.

```
import torch
```

## 概要
こちらの動きに合わせてゲーム内のキャラが動いたり、技を出すシステムを作った。<br>
プレイヤーはStreet Fighter Vという格闘ゲームにおける技の動きを真似て、それをカメラでリアルタイムで撮影する。<br>
プログラムは、撮影したものが何の技を繰り出しているかを自動で識別し、ゲーム内にその技のコマンドを送ることで技が出るという流れになっている。<br>
