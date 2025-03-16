import numpy as np
m1=int(input())
n1=int(input())
m2=int(input())
n2=int(input())
value1=[[0]*m1 for i in range(n1)]
value2=[[0]*m2 for i in range(n2)]
for i in range(n1):
    for j in range(m1):
        a1=int(input())
        value1[i][j]=a1
for i in range(n2):
    for j in range(m2):
        a2=int(input())
        value2[i][j]=a2
A = np.array(value1)
B = np.array(value2)
print(A)
print(B)
print(A+B)
print(A.dot(B))
