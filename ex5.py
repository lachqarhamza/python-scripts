a = input("enter a\n")
b = input("enter b\n")
# cast a and b to int
a = int(a)
b = int(b)
while b != 0:
    r = a % b
    a, b = b, r
print (a)
