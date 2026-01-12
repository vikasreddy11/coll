n=int(input("Enter a number"))

org=n
sum=0

while n>0:
    dig=n%10
    sum=dig+sum
    n=n//10

print("sum of digts",sum)