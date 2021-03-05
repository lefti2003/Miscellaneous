# Rearrange an array to sort it such that you extract 2 numbers
# when summed is the largest possible number
# sorting occurs using the merge sort.

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


def merge_sort(array):

    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Recursive call
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))


def rearrange_digits(array):
    largest_sum_str = ''
    second_largest_sum_str = ''
    sorted_array = merge_sort(array)
    n = len(sorted_array) - 1
    ln = n + 1
    if ln == 1:
        return [array[0], 0]
    elif ln == 0:
        return [0, 0]
    else:
        while n >= 0:
            if ln % 2 != 0 and n == 0:
                max_val = sorted_array[n]
                largest_sum_str += str(max_val)
                break
            else:
                max_val = sorted_array[n]
                sec_max_val = sorted_array[n-1]
                largest_sum_str += str(max_val)
                second_largest_sum_str += str(sec_max_val)
                n -= 2

        max_sum = int(largest_sum_str)
        sec_max_sum = int(second_largest_sum_str)

        return [max_sum, sec_max_sum]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[5], [5]])
# Pass
test_function([[], []])
# Pass
test_function([[1, 2, 3, 4, 5], [542, 31]])
# Pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# Pass