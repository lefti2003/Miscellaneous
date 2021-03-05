#a = [5, 3, 7, 0, 10]
a = [10,7,3,5,0]
n = len(a)
print("unsorted list = ", a)

def sorted_list(a):
    for i in range(n-1):
        for j in range(n -i -1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return a

print("sorted list=", sorted_list(a))



