import sys

a=float(sys.argv[1])
b=float(sys.argv[2])
c=float(sys.argv[3])

s=(a+b+c)/2

area=(s*(s-a)*(s-b)*(s-c))**0.5

print("Area",area)

