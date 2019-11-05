"""

Given an array of integers, return a new array such that each element at index i of the new array is the product of all

the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1],

the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?


"""


def find_solution(temp_list):

    resul_list = list()
    counter = 0
    product = 1

    while counter < len(temp_list):

        for i in temp_list:
            if i == temp_list[counter]:
                continue
            else:
                product *= i

        resul_list.append(product)
        product = 1
        counter += 1

    return resul_list







input_list = list()

print("Please Enter the Array Values:\nPress q or Q to exit")

while True:

    value = input("Value:")

    if value == 'q' or value == 'Q':

        break

    else:

        input_list.append(int(value))

print("Original List: {} and Modified List: {}".format(input_list,find_solution(input_list)))
