import os
import re


cdir = os.path.dirname(__file__)
os.chdir(cdir)
os.getcwd()


with open("data03") as file:
    data = file.read().splitlines()

xmax = len(data[0])

def count_tree(right_step, down_step, data):
    counter = 0
    for i in range(1, len(data)//down_step):
        x = (right_step*i) % xmax
        y = down_step*i
        a = data[y][x]
        if a == '#':
            counter += 1
    return counter

multi = 1
for right, down in zip([1, 3, 5, 7, 1], [1, 1, 1, 1, 2]):
    count = count_tree(right, down, data)
    print(count)
    multi *= count
print('total multiplicated: ', multi)
