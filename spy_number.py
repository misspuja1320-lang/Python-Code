
n=int(input("Enter the number:"))
m=n
s=0
p=1
while(n!=0):
    r=n%10
    n=n//10
    s=s+r
    p=p*r
    
print("Sum of digit",s)
print("Product of digit",p)
if(p==s):
    print(m,"is spy number")
else:
    print(m,"not spy number")