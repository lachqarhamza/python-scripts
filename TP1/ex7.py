# the first formula
print ("change the value of n in the code to change precesion")
# pi will be the fial value of pi
pi = long long float(0)
# n is the precision
n = 1000000 # this value is changebale
for i in range(n):
    # even index elements are positive
    if i % 2 == 0:
        pi += 4 / (2 * i + 1)
    else:
        # odd index elements are negetive
        pi -= 4 / (2 * i + 1)
print("the first formula:\n pi= ", pi)
pi = 0.0
for i in range(n - 1, -1, -1):
    if i % 2 == 0:
        pi += 4 / (2 * i + 1)
    else:
        pi -= 4 / (2 * i + 1)
print("the first formula:\n pi= ", pi)
