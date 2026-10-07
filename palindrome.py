# Palindrome number

n=int(input("Enter the number:"))
m=n
p=0
while(n!=0):
    r=n%10
    n=n//10
    p=(p*10)+r
if(p==m):
   print("palindrome")
else:
    print("not palindrome")