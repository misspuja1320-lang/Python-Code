#  Transpose matrix

r=int(input("Enter the number of row:"))
c=int(input("Enter the number of column:"))
m=[]
count=1
for i in range(r):
    row=[]
    for j in range(c):
        val=int(input("Enter the value:"))
        row.append(val)
        count+=1
    m.append(row)
   
print("Matrix is:")
for row in m:
    print(row)
    
t=[]
for i in range(r):    
    row=[]
    for j in range(c):
        row.append(m[j][i])
    t.append(row)
        
print("Transpose matrix is:")
for row in t:
    print(row)
   