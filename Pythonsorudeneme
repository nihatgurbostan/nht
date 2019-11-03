def check_for_number(value):


    if sum([int(i) for i in str(value)]) == sum([int(i) for i in str(2*value)]) == sum([int(i) for i in str(3*value)]) == sum([int(i) for i in str(4*value)]) == sum([int(i) for i in str(5*value)]) == sum([int(i) for i in str(6*value)]):
        return True
    else:
        return False




results_list = list()
for i in range(1000000):
    if check_for_number(i):
        results_list.append(i)
print(results_list)

