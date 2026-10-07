# prime armstrong number a given range

n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
for i in range(n1,n2+1):
    c=0
    for j in range(2,i):
        if i%j==0:
            c=1
            break
        else:
            c=0
    if i!=1 and i!=2:
        if c==0:
            m=i
            count=0
            result=0
            while m!=0:
                count+=1
                m=m//10
            m=i
            while m!=0:
                r=m%10
                m=m//10
                result+=r**count
            if i==result:
                print(i)