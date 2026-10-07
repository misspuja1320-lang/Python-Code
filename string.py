# string and substring

s1=input("Enter first string: ")
s2=input("Enter second string: ")
l=[]
s=0
while True:
    p=s1.find(s2,s)
    if(p==-1):
        break
    l.append(p)
    s=p+1
if l:
    print(1)
else:
    print(-1)