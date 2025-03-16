import re

msg1 = str(input("請輸入字串："))


def parseString(string):
    phoneRule = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
    phoneNum = phoneRule.search(string)
    if phoneNum != None:
        print(string, '包含台灣手機號碼')
    else:
        print(string, '不包含台灣手機號碼')

parseString(msg1)


