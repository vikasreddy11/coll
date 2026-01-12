n=int(input("enter a number "))

org=n
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10

print("reverse",rev)

if rev==org:
    print("It is pal ")
else:
    print("It is not")