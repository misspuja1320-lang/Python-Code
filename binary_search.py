# Binary search

n = int(input("Enter the number of rows: "))
a = []
for i in range(0, n):
    p = int(input("Enter the value: "))
    a.append(p)
a.sort()
print("Sorted list:", a)

s = int(input("Enter the searching item: "))

beg = 0
end = n - 1
f = 0

while beg <= end:
    mid = (beg + end) // 2
    if a[mid] == s:
        print("Found at position:", mid)
        f = 1
        break
    elif a[mid] < s:
        beg = mid + 1
    else:
        end = mid - 1

if f == 1:
    print("Found")
else:
    print("not found")