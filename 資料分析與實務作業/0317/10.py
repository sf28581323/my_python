import numpy as np
value=[[0]*3 for i in range(3)]
for i in range(3):
    for j in range(3):
        a=int(input())
        value[i][j]=a
A = np.array(value)
print(A)
print('最小值的索引為',np.argmin(A))
print('最大值的索引為',np.argmax(A))

