def transpose_matrix(a):
    # calculate the transpose of the matrix
    t = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
    # print transpose of the matrix
    for row in t:
        print(row)
# uncomment the following lines to test
# a = [[1.2, 1.1, 1.5],
#    [2.1, 2.2, 2.3],
#    [3.1, 3.2, 3.3]]
# transpose_matrix(a)
