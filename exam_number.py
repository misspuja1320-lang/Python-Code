# WAP to implement list and list will be sorted according to their examination number.

n=int(input("enter the number:"))
l=[]
a=['roll no','score']

'''for i in range(n):
    r=input("enter the roll no:")
    s=input("enter the score:")
    l.append([r,s])
 '''
for i in range(n):
    b=[]
    for j in range(len(a)):
        if(j!=0):
            r=input("enter the roll no:")
            b.append(r)
        else:
            s=input("enter the score:")
            b.append(s)
    l.append(b)
print(a)
for i in l:
    print(i)

for i in range(n-1):
    for j in range(i+1,n):
        if(l[i][0]<l[j][0]):
            l[i],l[j]=l[j],l[i];

print("sorted number:")
for i in l:
    print(i[0],i[1])