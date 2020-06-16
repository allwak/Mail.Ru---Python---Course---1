import re as re
import sys

digit_string = sys.argv[1]
s = digit_string
s1 = re.findall("\d",s)
number = 0
for i in s1:
    number += int(i)
print(number)
