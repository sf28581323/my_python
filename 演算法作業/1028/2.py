import numpy as np
m=int(input())
n=int(input())
def transpose(value): 
    return [[i[j] for i in value] for j in range(0, len(value[0]))] 
value=[[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        a=int(input())
        value[i][j]=a
A = np.array(value)
print(A)
trans=transpose(value)
B = np.array(trans)
print(B)
