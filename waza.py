import win32api, win32con
from time import sleep

#技のコマンドを自動でキーボード入力するクラス
class Skill():
    def __init__(self, waza_index, sleep_time):
        self.waza_index = waza_index
        self.sleep_time = sleep_time

    def get_skill(self):
        if (self.waza_index == 0):  #波動拳
            print("Hadouken")
            win32api.keybd_event(83, 0, 0, 0)  # S
            sleep(self.sleep_time)
            win32api.keybd_event(68, 0, 0, 0)  # D
            sleep(self.sleep_time)
            win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(self.sleep_time)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(self.sleep_time)
            win32api.keybd_event(66, 0, 0, 0)  # B
            sleep(self.sleep_time)
            win32api.keybd_event(66, 0, win32con.KEYEVENTF_KEYUP, 0)

        if (self.waza_index == 1):  #肘打ち
            print("hizi_punch")
            win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(37, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(self.sleep_time)
            win32api.keybd_event(66, 0, 0, 0)  # B
            sleep(self.sleep_time)
            win32api.keybd_event(66, 0, win32con.KEYEVENTF_KEYUP, 0)

        if (self.waza_index == 2):  #左パンチ
            print("left_punch")
            win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(37, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(self.sleep_time)
            win32api.keybd_event(78, 0, 0, 0) # N
            sleep(self.sleep_time)
            win32api.keybd_event(78, 0, win32con.KEYEVENTF_KEYUP, 0)

        if (self.waza_index == 3):  #右パンチ
            print("right_punch")
            win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(37, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(self.sleep_time)
            win32api.keybd_event(74, 0, 0, 0) # J
            sleep(self.sleep_time)
            win32api.keybd_event(74, 0, win32con.KEYEVENTF_KEYUP, 0)

        if (self.waza_index == 4):  #左キック
            print("left kick")
            win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(37, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(self.sleep_time)
            win32api.keybd_event(89, 0, 0, 0) # Y
            sleep(self.sleep_time)
            win32api.keybd_event(89, 0, win32con.KEYEVENTF_KEYUP, 0)

        if (self.waza_index == 5):  #右キック
            print("right kick")
            win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(37, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(self.sleep_time)
            win32api.keybd_event(72, 0, 0, 0) # H
            sleep(self.sleep_time)
            win32api.keybd_event(72, 0, win32con.KEYEVENTF_KEYUP, 0)

        if (self.waza_index == 6):  #鎖骨割り
            print("sakotuwari")
            win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(37, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(self.sleep_time)
            win32api.keybd_event(68, 0, 0, 0)
            sleep(self.sleep_time)
            win32api.keybd_event(74, 0, 0, 0)
            sleep(self.sleep_time)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(self.sleep_time)
            win32api.keybd_event(74, 0, win32con.KEYEVENTF_KEYUP, 0)

        if (self.waza_index == 7):  #昇竜拳
            print("syoryuken")
            win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(37, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(self.sleep_time)
            win32api.keybd_event(68, 0, 0, 0)
            sleep(self.sleep_time)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(self.sleep_time)
            win32api.keybd_event(83, 0, 0, 0)
            sleep(self.sleep_time)
            win32api.keybd_event(68, 0, 0, 0)
            sleep(self.sleep_time)
            win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(self.sleep_time)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            sleep(self.sleep_time)
            win32api.keybd_event(66, 0, 0, 0)
            sleep(self.sleep_time)
            win32api.keybd_event(66, 0, win32con.KEYEVENTF_KEYUP, 0)

        if (self.waza_index == 8): #何も実行しない
            print("no")