# prepares the table that we'll work with
def prepare_table():
    t = []
    for i in range(-9, 10):
        t.append(i)
    return t
# checks if a number is zero
def is_zero(e):
    return e == 0
# checks if a number is positive
def is_pos(e):
    return e > 0
# checks if a number is negative
def is_neg(e):
    return e < 0
# calculate the frequency of each(-, 0, +)
def count_stats(t):
    z = p = n = 0
    for i in range(len(t)):
        if is_zero(t[i]):
            z += 1
        elif is_pos(t[i]):
            p += 1
        elif is_neg(t[i]):
            n += 1
    return [n, z, p]
# script to test
r = count_stats(prepare_table())
print("number of negatives: ", r[0])
print("number of zeros: ", r[1])
print("number of positives: ", r[2])
