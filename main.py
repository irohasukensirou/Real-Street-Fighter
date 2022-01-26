from win32con import TRUE
import cv2
import numpy as np
import torch
import win32api, win32con
from time import sleep
from openpose.body import Body
from waza import Skill
from waza import sleept_time
from make_angle import calc_angle
from net import Net

def left_move(all_peaks, pre_all_peaks, threshold):
    p = 0
    for i in range(18):
        if ((all_peaks[i][0][0] - threshold) > pre_all_peaks[i][0][0]):
            p += 1
    if p == 18:
        return TRUE

def right_move(all_peaks, pre_all_peaks, threshold):
    p = 0
    for i in range(18):
        if ((all_peaks[i][0][0] + threshold) < pre_all_peaks[i][0][0]):
            p += 1
    if p == 18:
        return TRUE

def jump_move(all_peaks, pre_all_peaks, threshold):
    p = 0
    for i in range(18):
        if ((all_peaks[i][0][1] + threshold) < pre_all_peaks[i][0][1]):
            p += 1
    if p == 18:
        return TRUE


device = "cuda" if torch.cuda.is_available() else "cpu"
pre_waza = -1
no_count = 0
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
    while True:
        ret, oriImg = cap.read()
        cv2.imshow('frame', oriImg)
        all_peaks = body_estimation(oriImg)
        data = []
        angle = calc_angle(all_peaks)
        data.append(angle)
        x = np.array(data)
        x = torch.from_numpy(x).float().to(device)
        y_pred = waza_model(x)
        max_index = torch.argmax(y_pred)
        waza_index = max_index.item()
        print(waza_index)
        if waza_index != pre_waza:
            skill = Skill(waza_index)
            skill.get_skill()
        pre_waza = waza_index
        if waza_index == 8:
            #移動認識
            no_count += 10
            if no_count >= 2:
                if left_move(all_peaks, pre_all_peaks, 20):
                    #左移動
                    win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
                    print("左移動")
                    win32api.keybd_event(65, 0, 0, 0)
                    pre_all_peaks = all_peaks
                elif right_move(all_peaks, pre_all_peaks, 20):
                    #右移動
                    win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
                    print("右移動")
                    win32api.keybd_event(68, 0, 0, 0)
                    pre_all_peaks = all_peaks
                elif jump_move(all_peaks, pre_all_peaks, 0):
                    #ジャンプ
                    win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)
                    print("ジャンプ")
                    win32api.keybd_event(87, 0, 0, 0)
                    sleep(sleept_time)
                    win32api.keybd_event(87, 0, win32con.KEYEVENTF_KEYUP, 0)
            else:
                pre_all_peaks = all_peaks

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
else:
    print("camera is not exist")