# Linear search

n = int(input("Enter the number of rows: "))
a = []
for i in range(0, n):
    p = int(input("Enter the value: "))
    a.append(p)
a.sort()
print("Sorted list:", a)

s = int(input("Enter the searching item: "))

f=0
for i in range(n):
    if a[i]==s:
        print("Found at position:",i)
        f=1
        break
if f==1:
    print("found")
else:
    print("not found")