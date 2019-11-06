"""
 Write a Python program to check if a given positive integer is a power of two

"""


def isInt(x):

    x = abs(x)

    if x > int(x):
        return False
    else:
        return True




def check_if_power_of_two(value):

    if value >= 1:
        if value == 1 or value == 2:
            return True
        else:
            while value != 2:
                value /= 2
                if isInt(value) == False :
                    return False
            return True
    else:
        if value == 0:
            return False

        while value < 1:
            value *= 2

        if value == 1:
            return True
        else:
            return False










while True:

    number = float(input("Please Enter the Number: "))
    print(number)
    if check_if_power_of_two(number):
        print("{} is the power of 2".format(number))
    else:
        print("{} is not the power of 2".format(number))

