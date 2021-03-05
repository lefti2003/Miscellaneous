def findminnum(a):
    min_num = a[0]
    for i in range(len(a) - 1):
        if min_num > a[i + 1]:
            # found a new max swap
            min_num = a[i + 1]
    return min_num

a = [7, 3, 10, 0, 5]

print("min num in list =", findminnum(a))