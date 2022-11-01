def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if input_list == []:
        return "No elements in array"
    if len(input_list) == 1 and input_list[0] == number:
        return 0
    if len(input_list) == 1 and input_list[0] != number:
        return -1
    pivot_index = find_pivot(input_list)
    if number >= input_list[0]:
        return binary_search(input_list[:pivot_index], number)
    else:
        return binary_search(input_list[pivot_index:], number) + pivot_index

def find_pivot(array):
    start_index = 0
    end_index = len(array) - 1
    midpoint = (start_index + end_index) // 2
    if array[midpoint - 1] > array[midpoint]:
        return midpoint
    elif array[midpoint] > array[midpoint + 1]:
        return midpoint + 1
    
def binary_search(array, number):
    start_index = 0
    end_index = len(array) - 1
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2  
        mid_element = array[mid_index]
        if number == mid_element:
            return mid_index
        
        elif number < mid_element:
            end_index = mid_index - 1                   
        
        else:                                           
            start_index = mid_index + 1
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

assert rotated_array_search([], 1) == "No elements in array"
assert rotated_array_search([1], 0) == -1
assert rotated_array_search([5,6,7,1,2,3,4], 10) == -1