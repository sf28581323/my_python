import re

msg = '1 cat, 2 dogs, 3 pigs, 4 swans'
pattern = '[aeiouAEIOU 2-5]'
txt = re.findall(pattern,msg)
print(txt)
