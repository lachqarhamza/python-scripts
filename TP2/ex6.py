def sum_matrices(a, b):
    r = [[a[i][j] + b[i][j] for j in range(len(a[0]))]
    for i in range(len(a))]
    return r
def substract_matrices(a, b):
    r = [[a[i][j] - b[i][j] for j in range(len(a[0]))]
    for i in range(len(a))]
    return r
def multiply_matrices(a, b):
    temp = []
    r = []
    for i in range(len(a)):
        for j in range(len(b[0])):
            s = 0
            for k in range(len(b)):
                s += a[i][k] * b[k][j]
            temp.append(s)
        r.append(temp)
        temp = []
    return r
# the following lines are for testing
# a = [[1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]]
# b = [[9, 8, 7],
#    [6, 5, 4],
#    [3, 2, 1]]
# change function_name by the name of
# the function to test
# test = function_name(a, b)
# for row in test:
#    print(row)
