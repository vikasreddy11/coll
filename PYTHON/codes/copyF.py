with open("1.txt","r") as f1:
    with open("2.txt","w") as f2:
        data=f1.read()
        f2.write(data)

print("copied sucessful" )

with open("2.txt","r") as f3:
    print(f3.read())