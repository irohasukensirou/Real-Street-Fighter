import win32api, win32con
from time import sleep
sleept_time = 0.05

#技のコマンドを自動でキーボード入力するクラス
class Skill():
    def __init__(self, predict_value):
        self.predict_value = predict_value

    def get_skill(self):
        if (self.predict_value == 0):  #波動拳
            print("Hadouken")
            win32api.keybd_event(83, 0, 0, 0)  # S
            sleep(sleept_time)
            win32api.keybd_event(68, 0, 0, 0)  # D
            sleep(sleept_time)
            win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(sleept_time)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(sleept_time)
            win32api.keybd_event(66, 0, 0, 0)  # B
            sleep(sleept_time)
            win32api.keybd_event(66, 0, win32con.KEYEVENTF_KEYUP, 0)

        if (self.predict_value == 1):  #肘打ち
            print("hizi_punch")
            win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(37, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(sleept_time)
            win32api.keybd_event(66, 0, 0, 0)  # B
            sleep(sleept_time)
            win32api.keybd_event(66, 0, win32con.KEYEVENTF_KEYUP, 0)

        if (self.predict_value == 2):  #左パンチ
            print("left_punch")
            win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(37, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(sleept_time)
            win32api.keybd_event(78, 0, 0, 0) # N
            sleep(sleept_time)
            win32api.keybd_event(78, 0, win32con.KEYEVENTF_KEYUP, 0)

        if (self.predict_value == 3):  #右パンチ
            print("right_punch")
            win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(37, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(sleept_time)
            win32api.keybd_event(74, 0, 0, 0) # J
            sleep(sleept_time)
            win32api.keybd_event(74, 0, win32con.KEYEVENTF_KEYUP, 0)

        if (self.predict_value == 4):  #左キック
            print("left kick")
            win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(37, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(sleept_time)
            win32api.keybd_event(89, 0, 0, 0) # Y
            sleep(sleept_time)
            win32api.keybd_event(89, 0, win32con.KEYEVENTF_KEYUP, 0)

        if (self.predict_value == 5):  #右キック
            print("right kick")
            win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(37, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(sleept_time)
            win32api.keybd_event(72, 0, 0, 0) # H
            sleep(sleept_time)
            win32api.keybd_event(72, 0, win32con.KEYEVENTF_KEYUP, 0)

        if (self.predict_value == 6):  #鎖骨割り
            print("sakotuwari")
            win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(37, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(sleept_time)
            win32api.keybd_event(68, 0, 0, 0)
            sleep(sleept_time)
            win32api.keybd_event(74, 0, 0, 0)
            sleep(sleept_time)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(sleept_time)
            win32api.keybd_event(74, 0, win32con.KEYEVENTF_KEYUP, 0)

        if (self.predict_value == 7):  #昇竜拳
            print("syoryuken")
            win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(37, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(sleept_time)
            win32api.keybd_event(68, 0, 0, 0)
            sleep(sleept_time)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(sleept_time)
            win32api.keybd_event(83, 0, 0, 0)
            sleep(sleept_time)
            win32api.keybd_event(68, 0, 0, 0)
            sleep(sleept_time)
            win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(sleept_time)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(sleept_time)
            win32api.keybd_event(66, 0, 0, 0)
            sleep(sleept_time)
            win32api.keybd_event(66, 0, win32con.KEYEVENTF_KEYUP, 0)

        if (self.predict_value == 8): #何も実行しない
            print("no")