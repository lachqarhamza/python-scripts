i = 1
while i <= 5:
    a = input("enter your choice:\n")
    a = int(a)
    if (a == 0):
        print("gagne")
        i = 7
    i += 1
if (i == 6):
    print("perdu")
