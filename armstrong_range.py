# Armstrong number given a range

n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
for i in range(n1,n2+1):
    s,c=0,0
    m=n=i
    while(n!=0):
        n=n//10
        c+=1
    while(m!=0):
        r=m%10
        m=m//10
        s=s+(r**c)
    if(s==i):
        print(i,"is armstrong")