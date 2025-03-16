buy = int(input('請輸入購買金額:'))
if buy>=100000:
    pay = buy * 0.85
    print('需付',pay,'元')
elif 100000>buy>=50000:
    pay = buy * 0.9
    print('需付',pay,'元')
elif 50000>buy>=10000:
    pay = buy * 0.95
    print('需付',pay,'元')
elif buy<10000:
    pay = buy
    print('需付',pay,'元')
else:
    print('錯誤')
