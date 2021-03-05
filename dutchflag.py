# Sorts an array of 0's, 1's, 2's
# Ex: input : [0,0,2,2,2,1,1,1]
# output: [0,0,1,1,1,2,2,2]
def merge(left, right):

    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):

        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def sort_012(array):

    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Recursive call
    return merge(
        left=sort_012(array[:midpoint]),
        right=sort_012(array[midpoint:]))


def test_function(test_case):
    sorted_array = sort_012(test_case)
    if len(test_case) > 0:
        if sorted_array == sorted(test_case):
            print("Pass")
        else:
            print("Fail")


test_function([])
# Nothing to sort no valid element in array
test_function([0])
# Pass
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
# Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# Pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# Pass
