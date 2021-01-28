def print_matrice(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j], end='  ')
        print("\n")
# uncomment the following lines to test
# a = [[1.2, 1.1, 1.5],
#     [2.1, 2.2, 2.3],
#     [3.1, 3.2, 3.3]]
# print_matrice(a)
