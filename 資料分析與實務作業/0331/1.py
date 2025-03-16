import re

msg1 = 'I love Ming-Chi: 是大陸手機號碼'
msg2 = '0932-999-199: 是大陸手機號碼'
msg3 = '133-1234-1234: 是大陸手機號碼'

def parseString(string):
    phoneRule = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
    phoneNum = phoneRule.search(string)
    if phoneNum != None:
        print(string, 'True')
    else:
        print(string, 'False')

parseString(msg1)
parseString(msg2)
parseString(msg3)

