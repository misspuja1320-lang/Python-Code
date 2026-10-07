# Palindrome number given a range

n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
print("palindrome number :")
for i in range(n1,n2+1):
    m=i
    p=0
    while(m!=0):
        r=m%10
        m=m//10
        p=(p*10)+r
    if(p==i):
        print(i,end=" ")