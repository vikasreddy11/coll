for num in range(100,201):

    temp=num
    Sum=0

    while temp>0:
        dig=temp%10
        Sum=Sum+dig
        temp=temp//10

    if Sum%2!=0:
        print(num)