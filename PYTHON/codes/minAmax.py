user=input("Enter number sperated spaces")
nums=list(map(float,user.split()))

Max=nums[0]
Min=nums[0]

for i in nums:
    if Max<i:
        Max=i
    if Min>i:
        Min=i

print("Maximun ",Max)
print("Minimun ",Min)