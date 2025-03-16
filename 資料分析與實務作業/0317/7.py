import math
a = int(input())
b = int(input())
c = int(input())
def quadratic(a,b,c):
    key=b**2-4*a*c
    if key>0:
        x1=(-b+math.sqrt(key))/2*a
        x2=(-b-math.sqrt(key))/2*a
    if key==0:
        x1=-b/2*a
        x2=x1
    if key<0:
        print('方程無解')
        return(None,None)
    return (x1,x2)
print(quadratic(a,b,c))
