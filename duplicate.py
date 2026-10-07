# wap to remmove and count duplicate element from the list.

n=int(input("enter number:"))
l=[]
for i in range(n):
    v=int(input("enter the value:"))
    l.append(v)
print("List=",l)

s=[]
for i in l:
    if(i not in s):
        s.append(i)
        
print("modify list:")
for i in s:
    print(i)
    
print("count duplicate value:")
c={}
for i in l:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
for i in c:
    if(c[i]!=1):
        print(i,":",c[i])