a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = a
y = b

while b != 0:
    temp = b
    b = a % b
    a = temp

gcd = a
print("GCD is:", gcd)
lcm = (x * y) // gcd
print("LCM is:", lcm)
