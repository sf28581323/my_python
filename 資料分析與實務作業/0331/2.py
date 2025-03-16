import re

msg1 = 'Please call my secretary using 0930-919-919 or 0952-001-001'
msg2 = '請明天17:30和我一起參加明志科大教師節晚餐'
msg3 = '請明天17:30和我一起參加明志科大教師節晚餐, 可用0933-080-080聯絡我'

def parseString(string):
    pattern = r'\d{4}-\d{3}-\d{3}'
    phoneNum = re.search(pattern, string)
    if phoneNum != None:
        print('電話號碼是: %s' % phoneNum.group())
    else:
        print('%s 字串不含電話號碼' % string)

parseString(msg1)
parseString(msg2)
parseString(msg3)
