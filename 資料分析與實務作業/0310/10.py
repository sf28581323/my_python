a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
if a*d-b*c == 0:
    print('無解')
else:
    x = (e*d-b*f)/(a*d-b*c)
    y = (a*f-e*c)/(a*d-b*c)
    print('x =',x)
    print('y =',y)
