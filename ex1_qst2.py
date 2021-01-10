a = input("enter a\n")
b = input("enter b\n")
# cast a and b to int
a = int(a)
b = int(b)
# take the small and the big variable
if (a > b):
    # m is the small variable
    m = b
    # M is the big variable
    M = a
else:
    m = a
    M = b
# seperate the result output
print("odd numbers between", a, "and", b, "are:")
# initialize a sum variable with 0
s = 0
# initialize the count variable
count = 0
# start the loop
m += 1
while m < M:
    if (m % 2 != 0):
        print(m)
        s += m
        count += 1
    m += 1
if (count != 0):
    mean = float(s)/count
else:
    print("-- no odd numbers --")
    mean = 0
print("their sum is:", s)
print("their mean is:", mean)
