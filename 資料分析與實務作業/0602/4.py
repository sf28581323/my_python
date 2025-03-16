import numpy as np

a = np.loadtxt('weatherTaipei.txt', skiprows=1,usecols=(1, 2), dtype=int,delimiter=',')
print('最高溫度為',a.max())
print('平均溫度為',a.mean())
