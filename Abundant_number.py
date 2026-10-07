# Abundant number

n=int(input("Enter the number:"))
s=0
print("The factorial number:")
for i in range(1,n):
    if(n%i==0):
        print(i,"",end='')
        s=s+i
print("\nSum of factors are=",s)
if(s>n):
    print(n,"is abundant number")
else:
    print(n,"is not abundant number")