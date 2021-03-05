# data structure used in this question is an unsorted array
# and the return is a tuple of min and max.

import sys
import random


def get_min_max(ints):
    maxint = sys.maxsize
    # Added minint = -float('inf')
    minint = -float('inf')
    # if the array is empty return a tuple (None, None)
    if len(ints) == 0:
        print('Size of array is 0')
        return None, None
    # if the array has 1 element then the min = max
    elif len(ints) == 1:
        return ints[0], ints[0]
    else:
        for i in range(len(ints)):
            if ints[i] < maxint:
                maxint = ints[i]
            if ints[i] > minint:
                minint = ints[i]
        minint, maxint = maxint, minint

        return minint, maxint


# Example Test Case of Ten Integers


l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
# Pass

l1 = [i for i in range(0, 25)]  # a list containing 0 - 9
random.shuffle(l1)

print ("Pass" if ((0, 24) == get_min_max(l1)) else "Fail")
# Pass

l2 = [1]
print("Pass" if ((1, 1) == get_min_max(l2)) else "Fail")
# Pass

l3 = []
print(get_min_max(l3))
# Size of array is 0
# (None, None)

l4 = [i for i in range(-200000, -200)]
random.shuffle(l4)
print("Pass" if ((-200000, -201) == get_min_max(l4)) else "Fail")