def read_array_10():
    # init the list
    l = []
    i = 0
    print("enter the list's elements\n")
    while i < 10:
        # read the element from standard input
        e = float(input())
        # add the element to the list
        l.append(e)
        i += 1
    # reverse the list
    i = 0
    j = 9
    while i < j:
        temp = l[i]
        l[i] = l[j]
        l[j] = temp
        i += 1
        j -= 1
    # print the list
    print(l)
# to test the function uncomment the line bellow
# read_array_10(i)
