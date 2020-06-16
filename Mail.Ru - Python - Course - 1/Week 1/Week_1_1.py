import re as re
import sys

digit_string = sys.argv[0]

print(digit_string)

s = '859'
s1 = re.findall("\d",s)
print(s1)
number = sum([int(i) for i in s1])
print(number)
