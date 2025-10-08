import pandas as pd
import numpy as np

def directional_change(close: np.array, high: np.array, low: np.array, sigma: float):
    up_zig = True
    tmp_max = high[0]
    tmp_min = low[0]
    tmp_max_i = 0
    tmp_min_i = 0
    tops = []
    bottoms = []
    for i in range(len(close)):
        if up_zig:
            if high[i] > tmp_max:
                tmp_max = high[i]
                tmp_max_i = i
            elif close[i] < tmp_max - tmp_max * sigma:
                top = [i, tmp_max_i, tmp_max]
                tops.append(top)
                up_zig = False
                tmp_min = low[i]
                tmp_min_i = i
        else:
            if low[i] < tmp_min:
                tmp_min = low[i]
                tmp_min_i = i
            elif close[i] > tmp_min + tmp_min * sigma:
                bottom = [i, tmp_min_i, tmp_min]
                bottoms.append(bottom)
                up_zig = True
                tmp_max = high[i]
                tmp_max_i = i
    return tops, bottoms

def get_extremes(ohlc: pd.DataFrame, sigma: float):
    tops, bottoms = directional_change(ohlc['close'], ohlc['high'], ohlc['low'], sigma)
    tops = pd.DataFrame(tops, columns=['conf_i', 'ext_i', 'ext_p'])
    bottoms = pd.DataFrame(bottoms, columns=['conf_i', 'ext_i', 'ext_p'])
    tops['type'] = 1
    bottoms['type'] = -1
    extremes = pd.concat([tops, bottoms])
    extremes = extremes.set_index('conf_i')
    extremes = extremes.sort_index()
    return extremes