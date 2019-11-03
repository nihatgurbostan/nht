

def check_for_number(value):
    list_value   = [int(i) for i in str(value)]
    list_valuex2 = [int(i) for i in str(2*value)]
    list_valuex3 = [int(i) for i in str(3*value)]
    list_valuex4 = [int(i) for i in str(4*value)]
    list_valuex5 = [int(i) for i in str(5*value)]
    list_valuex6 = [int(i) for i in str(6*value)]
    
    list_value.sort()
    list_valuex2.sort()
    list_valuex3.sort()
    list_valuex4.sort()
    list_valuex5.sort()
    list_valuex6.sort()

    if (list_value == list_valuex2 and len(list_value) == len(list_valuex2)) and (list_value == list_valuex3 and len(list_value) == len(list_valuex3)) and (list_value == list_valuex4 and len(list_value) == len(list_valuex4)) and (list_value == list_valuex5 and len(list_value) == len(list_valuex5)) and (list_value == list_valuex6 and len(list_value) == len(list_valuex6)):
        return True
    else:
        return False


results_list = list()

for i in range(1,1000000):

    if check_for_number(i):
        results_list.append(i)

print(results_list)










