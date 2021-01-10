a = input("enter a\n")
b = input("enter b\n")
# cast a and b to int
a = int(a)
b = int(b)
if (a < 0 or b < 0):
    print("-- enter an integer --")
elif (a > b):
    # take the small and the big variable
    # m is the small variable
    m = b
    # M is the big variable
    M = a
else:
    m = a
    M = b
if (a >= 0 and b >= 0):
    # seperate the result output
    print("integers between", m, "and", M, "are:")
    # initialize a sum variable with 0
    s = 0
    # initialize the count variable with 0
    count = 0
    # start the loop
    for i in range(m + 1, M, 1):
        print(i)
        s += i
        count += 1
    if (count != 0):
        mean = float(s) / count
    else:
        print ("-- no results --")
        mean = 0.0
    print("their sum is:", s)
    print("their mean is:", mean)
