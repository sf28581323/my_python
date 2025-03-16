x = int(input('x = '))
n = int(input('n = '))

def e_x(n):
    factor = 1
    Sum = 1
    for i in range(1,n+1):
        factor *= i
        a = (x**i)/factor
        Sum += a
    return Sum

print(e_x(n))
