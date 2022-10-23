

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    ints_max = ints[1]
    ints_min = ints[0]
    for integer in ints:
        if integer <= ints_min:
            ints_min = integer
        if integer >= ints_max:
            ints_max = integer
    return (ints_min, ints_max)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")