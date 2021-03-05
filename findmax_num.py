def findmaxnum(a):
    max_num = a[0]
    for i in range(len(a) - 1):
        if max_num < a[i + 1]:
            # found a new max swap
            max_num = a[i + 1]
    return max_num

a = [7, 3, 10, 5, 0]

print("max num in list=", findmaxnum(a))

