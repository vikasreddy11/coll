data={}
n=int(input("enter a number:"))

for i in range(n):
    keys=input("enter key:")
    values=input("Enter values:")
    data[keys]=values

print("keys",data.keys())
print("values",data.values())
print("items",data.items())