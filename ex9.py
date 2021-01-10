# initialize i variable with 4
i = 4
# start the loop
while i > 0:
    j = i
    while j > 0:
        if (j == 1):
            print("*")
        else:
            # end = '' used to force the program
            # to cary on printing * in the same line
            print("* ", end = '')
        j -= 1
    i -= 1
