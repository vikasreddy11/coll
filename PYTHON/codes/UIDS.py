set1_u=input("Enter number seperated by spaces")
set1=set(map(int,set1_u.split()))

set2_u=input("Enter number seperated by spaces")
set2=set(map(int,set2_u.split()))

print("set 1",set1)
print("set 2",set2)

print("Union",set1.union(set2))
print("intersection",set1.intersection(set2))
print("differencce (set1-set2)",set1.difference(set2))
print("differencce (set2-set1)",set2.difference(set1))
print(" symmetric differencce (set1-set2)",set1.symmetric_differencedifference(set2))
