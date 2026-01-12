user=input("Enter number sperated spaces")
nums=list(map(float,user.split()))
found=False

key=int(input("enter to searched"))

for i in range(len(nums)):
    if nums[i]==key:
        found=True
        break

if found:
    print("Found")
else:
    print("not found")
