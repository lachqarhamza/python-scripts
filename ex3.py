n = input("enter an integer:\n")
n = int(n)
result = 1
i = 1
if (n < 0):
    print("-- enter an integer --")
elif (n == 0 or n == 1):
    print("1")
else:
    while i <= n:
        result *= i
        i += 1
    print(result)
