import pandas as pd

n=int(input("Enter a number"))


data={
    'Name': [],
    'Age':[],
    'Marks':[]
}

for i in range(n):
    Name=(input("Enter name"))
    Age=int(input("Enter age"))
    Marks=int(input("Enter marks"))

    data["Name"].append(Name)
    data["Age"].append(Age)
    data["Marks"].append(Marks)

df=pd.DataFrame(data)

print(df)