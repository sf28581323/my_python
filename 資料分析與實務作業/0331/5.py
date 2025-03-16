import re

def searchStr(pattern, msg):
    txt = re.search(pattern, msg)
    if txt == None:
        print('搜尋失敗', txt)
    else:
        print('搜尋成功', txt.group())

msg1 = 'son'
msg2 = 'sonson'
msg3 = 'sonsonson'
msg4 = 'sonsonsonson'
msg5 = 'sonsonsonsonson'
pattern1 = '(son){2,}'
pattern2 = '(son){,5}'
print('以下用(son){2,}測試')
searchStr(pattern1,msg1)
searchStr(pattern1,msg2)
searchStr(pattern1,msg3)
searchStr(pattern1,msg4)
searchStr(pattern1,msg5)
print('以下用(son){,5}測試')
searchStr(pattern2,msg1)
searchStr(pattern2,msg2)
searchStr(pattern2,msg3)
searchStr(pattern2,msg4)
searchStr(pattern2,msg5)
