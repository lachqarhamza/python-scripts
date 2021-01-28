def odd_table():
    i = 3
    t = []
    while i <= 21:
        if i % 2 != 0:
            t.append(i)
        i += 1
    return t
def print_table(t):
    print("table is: ", t)
def sum_table(t):
    s = 0
    for i in t:
        s += i
    return s
def print_sum(t):
    print("sum is = ", sum_table(t))
def print_avg(t):
    print("avg = ", sum_table(t) / len(t))
print_table(odd_table())
print_sum(odd_table())
print_avg(odd_table())
