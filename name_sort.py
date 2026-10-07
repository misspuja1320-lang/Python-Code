# wap to implement name sorting.

n=int(input("enter the number:"))
l=[]
for i in range(n):
    name=input("enter the name:")
    l.append(name)
print(l)

for i in range(n-1):
    for j in range(i+1,n):
        if(l[i]>l[j]):
            l[i],l[j]=l[j],l[i];

print("sorted names:")
for i in l:
    print(i)