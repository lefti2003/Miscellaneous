# returns the floor (square root) of a positive integer

def sqrt(number):

    if number >= 0:
        if number == 0 or number == 1:
            return number

    # Do Binary Search for floor(sqrt(x))
        start = 1
        end = number
        while start <= end:
            mid = (start + end) // 2

            if mid * mid == number:
                return mid

            elif mid * mid < number:
                start = mid + 1
                ans = mid
            else:
                end = mid - 1

        return ans
    else:
        print("Cannot take the square root of a negative number")
        return -1

print(sqrt(-1))
# Cannot take the square root of a negative number
# -1
print("Pass" if (3 == sqrt(9)) else "Fail")
#Pass
print("Pass" if (0 == sqrt(0)) else "Fail")
#Pass
print("Pass" if (4 == sqrt(16)) else "Fail")
#Pass
print("Pass" if (1 == sqrt(1)) else "Fail")
#Pass
print("Pass" if (5 == sqrt(27)) else "Fail")
#Pass
print(sqrt(100000000))
# 10000