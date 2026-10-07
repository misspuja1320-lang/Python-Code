r1=int(input("Enter the first row number:"))
c1=int(input("Enter the first column number:"))
r2=int(input("enter the second row number:"))
c2=int(input("Enter the second column number:"))

print("Enter the first matrix")
a=[]
for i in range(r1):
    r=[]
    for j in range(c1):
        val=int(input("Enter the values:"))
        r.append(val)
    a.append(r)
for r in a:
    print(r)
    
print("Enter the second matrix")
b=[]
for i in range(r2):
    r=[]
    for j in range(c2):
        val=int(input("Enter the values:"))
        r.append(val)
    b.append(r)
for r in b:
    print(r)
    
result=[]
for i in range(r1):
    r=[]
    for j in range(c2):
        c=0
        for k in range(c1):
            c+=a[i][k]*b[k][j]
        r.append(c)
    result.append(r)
    
print("Result matrix multiplication:")
for r in result:
    print(r)