# This mentor help post informed the answer here: https://knowledge.udacity.com/questions/743770

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0:
        return "There are no numbers in the input list."
    if len(input_list) == 1:
        return input_list[0]
    copied_array = input_list.copy()
    first_integer = ''
    second_integer = ''
    maximum = 0
    for index in range(len(input_list)):
        maximum = max(copied_array)
        if index % 2 == 0:
            first_integer += str(maximum)
        else:
            second_integer += str(maximum)
        copied_array.remove(maximum)
        print(first_integer, second_integer)
        
    return [int(first_integer), int(second_integer)]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    print(output, solution)
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
