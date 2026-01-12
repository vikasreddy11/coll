import pandas as pd 
import matplotlib.pyplot as plt

df=pd.read_csv("employee.csv")

print(df)

plt.figure()
plt.plot(df['EId'],df['ESal'])
plt.title("Line plot")
plt.xlabel('E id')
plt.ylabel('E salary')
plt.grid()
plt.show()

plt.bar(df['EId'],df['ESal'])
plt.title("Bar plot")
plt.xlabel("e id")
plt.ylabel("e sal")
plt.show()

plt.hist(df['EId'])
plt.title('hist plot')
plt.xlabel('E id')
plt.show()

plt.boxplot(df['EId'])
plt.title("box plot")
plt.xlabel('Eid')
plt.show()