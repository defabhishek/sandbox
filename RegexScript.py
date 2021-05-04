import re
a = 'abhishek@gmail.com h9%'
A_B = 3
print(re.findall('@([^ ]*)',a))
print(re.findall('h[A-z,0-9]+',a))
print(re.findall("(b.+)@",a))
A_B = 4
print(A_B)