import numpy as np
list = []
for i in range(10):
    x=int(input())
    list.append(x)
median = np.median(list)
average = np.mean(list)
counts = np.bincount(list)
print(list)
print('中位數為',median)
print('平均數為',average)
print('眾數為',np.argmax(counts))

