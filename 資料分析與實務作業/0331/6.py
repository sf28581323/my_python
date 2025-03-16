import re

def searchStr(pattern, msg):
    txt = re.search(pattern, msg)
    if txt == None:
        print('搜尋失敗', txt)
    else:
        print('搜尋成功', txt.group())

msg = 'sonsonsonsonson'
pattern1 = '(son){3,5}'
print('以下用(son){3,5}測試')
searchStr(pattern1,msg)
pattern2 = '(son){3,5}?'
print('以下用(son){3,5}?測試')
searchStr(pattern2,msg)

