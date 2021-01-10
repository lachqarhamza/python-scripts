a = input ("inter an integer:\n")
a = int(a)
if (a < 0):
    print ("-- enter a number greater than 0 --")
elif (a <= 2):
    print ("no")
else:
    i = 2
    # initialize a sum variable with 0
    s = 1
    while i < a:
        if (a % i == 0):
            s += i
        i += 1
    if (s == a):
        print("yes")
    else:
        print("no")
