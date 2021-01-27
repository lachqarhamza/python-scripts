def read_array_10():
    # init the list
    l = []
    i = 0
    s = 0
    print("enter the list's elements\n")
    while i < 10:
        # read the element from standard input
        e = float(input())
        # add the element to the list
        l.append(e)
        s += l[i]
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
    # print results
    print("the list is: ", l)
    print("sum = ", s)
    print("average = ", s/10)
# to test the function uncomment the line bellow
read_array_10()
