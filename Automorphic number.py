
num = int(input("Enter a number: "))
square = num * num
print(square)
n = num
m = 1
while n != 0:
    m = m * 10
    r = n % 10
    n = n // 10
square_r=square % m
if square_r == num:
    print(num, "is an Automorphic number")
else:
    print(num, "is not an Automorphic number")
