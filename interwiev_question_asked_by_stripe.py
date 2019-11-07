"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

"""


def find_missing_positive(coming_list):
    temp_list = list()
    least_positive = 1
    counter = 0
    for i in  coming_list:
        if i>0:
            temp_list.append(i)

    if len(temp_list) == 0:
        return 1

    temp_list.sort()

    while counter < len(temp_list):
        if counter +1 != temp_list[counter]:
            return counter+1
        counter += 1

    return temp_list[counter -1] +1



input_list = [1,2,3,4,8,9]

print(find_missing_positive(input_list))
