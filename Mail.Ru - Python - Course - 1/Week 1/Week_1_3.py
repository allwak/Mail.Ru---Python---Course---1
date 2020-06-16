import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = b*b - 4*a*c
d = d ** (1/2)
x1 = (0-b+d)/(2*a)
x2 = (0-b-d)/(2*a)

print(int(x1))
print(int(x2))
