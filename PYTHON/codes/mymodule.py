def Gcd(m,n):
    if m==0 and n==0:
        print("GCD is 0")

    if n==0:
        return m
    if m==0:
        return n
    
    while m!=n:
        if m>n:
            m=m-n
        if n>m:
            n=n-m
    return m


def Lcm(m,n):
    gcd=Gcd(m,n)
    lcm=(m*n)//gcd
    return lcm