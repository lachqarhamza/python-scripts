def min_max():
    # get the length of the list
    n = int(input("enter the number of elements :\n"))
    # get the list
    l = list(map(int, input("enter the elements :\n").strip().split()))[:n]
    i = 0
    m = M = 0
    # search for min and max
    while i < n:
        if l[i] < m:
            m = l[i]
        elif l[i] > M:
            M = l[i]
        i += 1
    # print results
    print("min = ", m, "max = ", M)
# to test the function uncomment the line bellow
# min_max()
