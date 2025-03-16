import re

msg = '''txt@deepstone.com.tw kkk@gmail.com
abc@me.com mymail@qq.com abc@abc@abc'''

pattern = r'''(
    [a-zA-Z0-9-.]+
    @
    [a-zA-Z0-9-.]+
    [\.]
    [a-zA-Z]{2,4}
    ([\.])?
    ([a-zA-Z]{2,4})?
    )'''

eMail = re.findall(pattern, msg, re.VERBOSE)
print(eMail)
