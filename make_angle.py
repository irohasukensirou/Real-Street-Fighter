import numpy as np

#人間の骨格の座標データを座標間の角度データに変換
def calc_angle(all_peaks):
    angle_list = []
    for i in range(18):
        if i == 1:
            continue
        else:
            angle = np.degrees(np.arctan2((all_peaks[i][0][1] - all_peaks[1][0][1]), (all_peaks[i][0][0] - all_peaks[1][0][0])))
            angle_list.append(angle)
    return angle_list