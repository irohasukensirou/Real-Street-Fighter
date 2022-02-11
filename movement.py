import win32api, win32con
from time import sleep
from waza import sleept_time

#左移動の判定を行う関数
def left_move(all_peaks, pre_all_peaks, threshold):
    p = 0
    for i in range(18):
        if ((all_peaks[i][0][0] - threshold) < pre_all_peaks[i][0][0]):
            p += 1
    if p == 18:
        return True

#右移動の判定を行う関数
def right_move(all_peaks, pre_all_peaks, threshold):
    p = 0
    for i in range(18):
        if ((all_peaks[i][0][0] + threshold) < pre_all_peaks[i][0][0]):
            p += 1
    if p == 18:
        return True

#ジャンプの判定を行う関数
def jump_move(all_peaks, pre_all_peaks, threshold):
    p = 0
    for i in range(18):
        if ((all_peaks[i][0][1] + threshold) < pre_all_peaks[i][0][1]):
            p += 1
    if p == 18:
        return True

#移動を実行する関数
def movement_exe(type_of_movement):
    #引数が0なら左移動、1なら右移動、2ならジャンプを実行
    if type_of_movement == 0:
        win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
        print("左移動")
        win32api.keybd_event(65, 0, 0, 0)
    
    elif type_of_movement == 1:
        win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
        print("右移動")
        win32api.keybd_event(68, 0, 0, 0)

    elif type_of_movement == 2:
        win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)
        print("ジャンプ")
        win32api.keybd_event(87, 0, 0, 0)
        sleep(sleept_time)
        win32api.keybd_event(87, 0, win32con.KEYEVENTF_KEYUP, 0)
