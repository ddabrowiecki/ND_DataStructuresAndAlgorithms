def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0:
        return 0
    if number == 1:
        return 1
    upper_bound = number // 2
    lower_bound = 1
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        if mid * mid == number or mid + 1 == upper_bound:
            return mid
        elif mid * mid > number:
            upper_bound = mid - 1
        elif mid * mid < number:
            lower_bound = mid + 1
            floor = lower_bound
    return floor

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

assert sqrt(0) == 0
assert sqrt(1) == 1
assert sqrt(7784) == 88