import numpy as np

user=input("enter numbers sperated by spaces")
nums=np.array(list(map(float,user.split())))

print("Mean:",np.mean(nums))
print("std:",np.std(nums))
print("Max:",np.max(nums))
print("Min:",np.min(nums))