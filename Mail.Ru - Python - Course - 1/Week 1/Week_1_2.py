import sys

num_steps = sys.argv[1]

s = num_steps
number = int(s)
grid  = "#"
space = " "
for i in range(1,number+1):
    print((number-i)*space + i*grid)
