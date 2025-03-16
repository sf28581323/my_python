import re

msg = '''02-88223349, (02)-26669999, 02-29998888 ext 123,
        12345678, 02 33887766 ext. 12222,
        02-1234567, 02-123456789, 23-123456'''
pattern = r'''(
    (\d{2}|\(\d{2}\))?
    (\s|-)?
    \d{7,8}
    (\s*(ext|ext.)\s*\d{2,4})?
    )'''
phoneNum = re.findall(pattern, msg, re.VERBOSE)
print(phoneNum)
