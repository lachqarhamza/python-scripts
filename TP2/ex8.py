def is_janus(n):
    # initialize a list
    l = []
    temp = n
    result = True
    # store the number in the list
    while n != 0:
        l.append(n % 10)
        n = n // 10
    i = 0
    j = len(l) - 1
    # test if is janus
    while i < j and result:
        if l[i] != l[j]:
            result = False
        i += 1
        j -= 1
    # print results
    if result:
        print(temp, "is janus")
    else:
        print(temp, "isn't janus")
# uncomment the line bellow for test
is_janus(111211)
