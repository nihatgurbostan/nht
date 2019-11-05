"""

Given an array of integers, return a new array such that each element at index i of the new array is the product of all

the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1],

the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?


"""


def find_solution(temp_list):
    result_list = list()
    product = 1
    counter = 0

    while counter < len(temp_list):
        for i in temp_list:
            product *= i
        result_list.append(int(product/temp_list[counter]))
        product = 1
        counter += 1

    return result_list




example = [1,2,3,4,5]

print(find_solution(example))
