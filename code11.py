import os
import numpy as np

cdir = os.path.dirname(__file__)
os.chdir(cdir)
os.getcwd()

with open("data11") as file:
    data = file.read().split('\n')
    # data = file.readlines()
data2 = list()
for line in data:
    data2.append([i for i in line])

data2 = np.array(data2)


def min_max(line_num, data_len):
    if line_num == 0:
        return 0, 2
    elif line_num == data_len:
        return data_len - 1, data_len
    else:
        return line_num - 1, line_num + 2


def find_surround(i, j, data):
    # print(i, j)
    left, right, top, down = '', '', '', ''
    for n in reversed(data[i, :j]):
        if n != '.':
            left = n
            break
    for n in data[i, j+1:]:
        if n != '.':
            right = n
            break
    for n in reversed(data[:i, j]):
        if n != '.':
            top = n
            break
    for n in data[i+1:, j]:
        if n != '.':
            down = n
            break
    left_top, right_top, left_down, right_down = '', '', '', ''
    for n in range(1, min(i, j) + 1):
        if data[i - n, j - n] != '.':
            left_top = data[i - n, j - n]
            break
    for n in range(1, min(i, len(data[i])-1 - j)+1):
        if data[i - n, j + n] != '.':
            right_top = data[i - n, j + n]
            break
    for n in range(1, min(len(data) -1 - i, len(data[i])-1 - j)+1):
        if data[i + n, j + n] != '.':
            right_down = data[i + n, j + n]
            break
    for n in range(1, min(len(data)-1 - i, j)+1):
        if data[i + n, j - n] != '.':
            left_down = data[i + n, j - n]
            break
    return [right, left, top, down, right_top, right_down, left_top, left_down]


def update_room(data):
    new_state = data.copy()
    for l, line in enumerate(data):
        for s, spot in enumerate(line):
            if spot == '.':
                new_state[l, s] = '.'
                continue
            miny, maxy = min_max(l, len(data))
            minx, maxx = min_max(s, len(line))
            surround = [i for i in data[miny:maxy, minx:maxx].flat]
            surround.remove(spot)
            if spot == 'L' and not surround.count('#'):
                new_state[l, s] = '#'
            if spot == '#' and surround.count('#') > 3:
                new_state[l, s] = 'L'
    return new_state


def update_room_relaxed(data):
    new_state = data.copy()
    for l, line in enumerate(data):
        for s, spot in enumerate(line):
            if spot == '.':
                new_state[l, s] = '.'
                continue
            miny, maxy = min_max(l, len(data))
            minx, maxx = min_max(s, len(line))
            surround = find_surround(l, s, data)
            if spot == 'L' and not surround.count('#'):
                new_state[l, s] = '#'
            if spot == '#' and surround.count('#') > 4:
                new_state[l, s] = 'L'
    return new_state


surround  = find_surround(9, 1, data2)
update = update_room(data2)
while not (update == data2).all():
    data2 = update.copy()
    # update = update_room(data2)
    update = update_room_relaxed(data2)
    # print((update == data2).all())

print('number of occupied seats: ', data2.flatten().tolist().count('#'))
