a=float(input("Enter coef of a"))
b=float(input("Enter coef of b"))
c=float(input("Enter coef of c"))

d=b**2-4*a*c

if d>0:
    print("roots are real and distint ")
    r1=(-b+d**0.5)/2*a
    r2=(-b-d**0.5)/2*a
    print(r1,r2)

elif d==0:
    print("Roots are real and equal")
    r1=(-b)/2*a
else:
    print("roots are imaginary")