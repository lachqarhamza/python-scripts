def pascal(d):
    t = []
    temp = []
    for i in range(d + 1):
        for j in range(i + 1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(t[i - 1][j] + t[i - 1][j - 1])
            print(temp[j], " ", end='')
        t.append(temp)
        temp = []
        print("\n")
# uncomment the line bellow to test this function
pascal(10)
