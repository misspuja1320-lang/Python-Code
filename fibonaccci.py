# fibonacci series upto n.

n=int(input("Enter the number:"))
a=0
b=1
while(a<=n):
    print(a,"",end='')
    c=a+b
    a=b
    b=c
