#Bubble sort

n = int(input("Enter the number of rows: "))
a = []
for i in range(0, n):
    p = int(input("Enter the value: "))
    a.append(p)
print("Original list:",a)
t=0
for i in range(n-1):
    for j in range(n-1-i):
        if a[j]>a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
print("Sorted list:",a)