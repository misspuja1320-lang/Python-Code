# Armstrong number

n=int(input("Enter the number:"))
c,s=0,0
k=m=n
while(n!=0):
    n=n//10
    c+=1
while(m!=0):
    r=m%10
    m=m//10
    s=s+pow(r,c)
if(s==k):
    print("armstrong")
else:
    print("not armstrong")