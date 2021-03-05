# Use binary search to search an array for a number

def rotated_array_search(arr, n, target):
    pivot = get_pivot(arr, 0, n - 1)

    # if the pivot is not found
    if pivot == -1:
        return binary_search(arr, 0, n - 1, target)

    if arr[pivot] == target:
        return pivot
    if arr[0] <= target:
        return binary_search(arr, 0, pivot - 1, target)
    return binary_search(arr, pivot + 1, n - 1, target)


def get_pivot(arr, low, high):
    # base cases
    if high < low:
        return -1
    if high == low:
        return low

    mid = int((low + high) / 2)

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1
    if arr[low] >= arr[mid]:
        return get_pivot(arr, low, mid - 1)
    return get_pivot(arr, mid + 1, high)


def binary_search(arr, low, high, target):
    if high < low:
        return -1

    mid = int((low + high) / 2)

    if target == arr[mid]:
        return mid
    if target > arr[mid]:
        return binary_search(arr, (mid + 1), high, target)
    return binary_search(arr, low, (mid - 1), target)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, len(input_list), number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# Pass
test_function([[1], 1])
# Pass