n=int(input("Enter a number :"))
prime=True
if n==2 or n==1:
    print("Prime")

else:

    for i in range(2,n):
        if n%i==0:
            prime=False
    if prime:
        print("prime")
    else:
        print("not prime")
          