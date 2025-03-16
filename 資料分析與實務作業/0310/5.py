t = int(input('1.攝氏-> 華氏. 2.華氏->攝氏.'))
if t == 1:
    print('請輸入溫度:',end = '\n')
    c = int(input())
    f = c * (9 / 5) + 32
    print('轉換的溫度為華氏',f,'度')
elif t == 2:
    print('請輸入溫度:',end = '\n')
    f = int(input())
    c = (f - 32) * (5 / 9)
    print('轉換的溫度為攝氏',c,'度')
else:
    print('錯誤')
    
