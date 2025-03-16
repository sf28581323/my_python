a = int(input())

if 100 <= a <= 999:
    a = a // 10 * 10
    print(a)
else:
    print('不是三位數')
