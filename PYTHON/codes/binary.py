user=(input("Enter a numbers sperated:"))
nums=list(map(float,user.split()))

key=float(input("Enter a number to search: "))

low=0
high=len(nums)-1

found=False

while low<=high:
    mid=(low+high)//2
    if nums[mid]==key:
        found=True
        print("Ele found at ",mid+1)
        break

    elif nums[mid]<key:
        low=mid+1
    else:
        high=mid-1

if not found:
    print("Ele not found")
