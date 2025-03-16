import numpy as np

a = np.random.randint(low=5,high=17,size=15)
X = a.reshape((3, 5))
X1 = X[[0,-1]][:,[0,-1]]
np.savetxt('EX3_2.txt', X1, fmt='%0.0f')
b = np.random.randint(low=5,high=17,size=15)
Y = b.reshape((3, 5))
Z = X+Y
print(X)
print('最大值為',X.max())
print('最小值為',X.min())
print('總和為',X.sum())
print('平均為',X.mean())
print(X1)
print(Y)
print(Z)
