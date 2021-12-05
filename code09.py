import os


def is_valid(number_to_validate, validation_list):
    for cur_num in validation_list:
        val_list = validation_list.copy()
        val_list.remove(cur_num)
        if (number_to_validate - cur_num) in val_list:
            return 1
    return 0


def find_weakness(data, number_to_validate):
    for i in range(0, len(data)):
        sum_ser = 0
        n = i
        while sum_ser < number_to_validate:
            n += 1
            sum_ser = sum(data[i:n])
        if sum_ser == number_to_validate:
            return data[i:n]
    return [-1, -1] # failed to find a weakness

cdir = os.path.dirname(__file__)
os.chdir(cdir)
os.getcwd()

with open("data09") as file:
    data = file.read().split('\n')

data = [int(i) for i in data]

len_val = 50

for i in range(0, len(data)-len_val):
    validation_list = data[i:i+len_val]
    number_to_validate = data[i+len_val]
    if not is_valid(number_to_validate, validation_list):
        print('this is not valid: ', number_to_validate)
        weakness_series = find_weakness(data, number_to_validate)
        print('sum of first and last: ', min(weakness_series) + max(weakness_series))
        break

