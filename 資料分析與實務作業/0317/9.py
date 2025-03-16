import numpy as np
value1=[[0]*3 for i in range(3)]
value2=[[0]*3 for i in range(3)]
for i in range(3):
    for j in range(3):
        a1=int(input())
        value1[i][j]=a1
for i in range(3):
    for j in range(3):
        a2=int(input())
        value2[i][j]=a2
A = np.array(value1)
B = np.array(value2)
print(A)
print(B)
print(A+B)
print(A.dot(B))
