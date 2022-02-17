import cv2
import numpy as np
import torch
import win32api, win32con
from time import sleep
from openpose.body import Body
from waza import Skill
from make_angle import calc_angle
from movement import left_move, right_move, jump_move, movement_exe
from net import Net

device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)

#骨格座標検出モデルの読み込み
body_estimation = Body('./model/body_pose_model.pth')

#技識別モデルの読み込み
waza_model = Net(input_dim=17, hidden_dim=255, n_layers=3).to(device)
waza_model.load_state_dict(torch.load("./model/waza_model.pth"))
waza_model.eval()

#カメラの読み込み
cap = cv2.VideoCapture(0)
cap.set(3, 200)
cap.set(4, 150)

#カメラの映像から技を識別し、ゲーム内で出力
if cap.isOpened():
    pre_waza_index = -1
    movement_flag = 0
    while True:
        #撮影した人物から骨格点データを取得
        ret, oriImg = cap.read()
        cv2.imshow('frame', oriImg)
        all_peaks = body_estimation(oriImg)
        #骨格点データを座標間の角度データに変換
        angle_data = calc_angle(all_peaks)
        X = np.array(angle_data).reshape(1, len(angle_data))
        X = torch.from_numpy(X).float().to(device)
        #技の識別
        y_pred = waza_model(X)
        max_index = torch.argmax(y_pred)
        waza_index = max_index.item()
        #技の出力
        if waza_index != pre_waza_index:
            skill = Skill(waza_index, sleep_time=0.05)
            skill.get_skill()
        pre_waza_index = waza_index

        #移動認識
        if waza_index == 8:
            if movement_flag == 1:
                if left_move(all_peaks, pre_all_peaks, 20):
                    #左移動
                    movement_exe(0)
                    pre_all_peaks = all_peaks
                elif right_move(all_peaks, pre_all_peaks, 20):
                    #右移動
                    movement_exe(1)
                    pre_all_peaks = all_peaks
                elif jump_move(all_peaks, pre_all_peaks, 0):
                    #ジャンプ
                    movement_exe(2)
            else:
                pre_all_peaks = all_peaks
                movement_flag = 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
else:
    print("camera is not exist")