s=set()

with open("sample.txt","r") as f1:
    s1=f1.read()

L=s1.split()

for i in L:
    s.add(i)

l=list(s)
l.sort()
print(l)