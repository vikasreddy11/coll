import numpy as np

r1=int(input("Enter a numbers for rows of M2:"))
c1=int(input("Enter a numbers for cols of M2:"))
print("Enter values row wise:")

A=[]

for i in range(r1):
    row=list(map(int,input().split()))
    A.append(row)


r2=int(input("Enter a numbers for rows of M2:"))
c2=int(input("Enter a numbers for cols of M2:"))
print("Enter values row wise:")

B=[]

for i in range(r2):
    row=list(map(int,input().split()))
    B.append(row)

A=np.array(A)
B=np.array(B)

if c1!=r2:
    print("MUl is not possible",exit())
else:
    c=np.matmul(A,B)

    print("matrix A",A)
    print("matrix B",B)
    print("multiplied matrix",c)