import re

msg1 = '0932895453'
msg2 = '09328ss453'
pattern = '^\d+$'
txt1 = re.findall(pattern,msg1)
txt2 = re.findall(pattern,msg2)
print(txt1)
print(txt2)
