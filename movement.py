#左移動の判断をする関数
def left_move(all_peaks, pre_all_peaks, threshold):
    p = 0
    for i in range(18):
        if ((all_peaks[i][0][0] - threshold) > pre_all_peaks[i][0][0]):
            p += 1
    if p == 18:
        return True

#右移動の判断をする関数
def right_move(all_peaks, pre_all_peaks, threshold):
    p = 0
    for i in range(18):
        if ((all_peaks[i][0][0] + threshold) < pre_all_peaks[i][0][0]):
            p += 1
    if p == 18:
        return True

#ジャンプの判断をする関数
def jump_move(all_peaks, pre_all_peaks, threshold):
    p = 0
    for i in range(18):
        if ((all_peaks[i][0][1] + threshold) < pre_all_peaks[i][0][1]):
            p += 1
    if p == 18:
        return True