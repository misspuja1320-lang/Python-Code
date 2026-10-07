# wap to implement list and update it 5% extra of his gross salary whose salary less than 10000.

n=int(input("enter the number:"))
l=[]

'''for i in range(n):
    s=int(input("enter salary:"))
    if(s<10000):
        s+=(s*.5)
    l.append(s)
for i in l:
    print(i)
    
'''    
    
a=['name','salary']

for i in range(n):
    b=[]
    for j in range(len(a)):
        if(j==0):
            n=input("enter the name:")
            b.append(n)
        else:
            s=int(input("enter the salary:"))
            if(s<10000):
                s=s+(s*(5/100))
            b.append(s)
    l.append(b)
    
for i in l:
    print(i)
    

    