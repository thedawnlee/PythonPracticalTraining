import random
import numpy as np
import scipy.signal as signal

#一维中值滤波
x = np.arange(0,100,10)
random.shuffle(x)
print(x)

print(signal.medfilt(x, 3))
#二维中值滤波
#2d方式中值滤波
#这种方式只支持int8 float32 float64
