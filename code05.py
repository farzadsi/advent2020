import os

cdir = os.path.dirname(__file__)
os.chdir(cdir)
os.getcwd()

with open("data05") as file:
    data = file.read().splitlines()


def code(min, max, code):
    if code in ['F', 'L']:
        max = int(max - (max-min)/2)
    if code in ['B', 'R']:
        min = round(min + (max-min)/2)
    return min, max


highest_ID = 0
all_seats = list()
for board in data:
    min_val, max_val = 0, 127
    for i in range(7):
        min_val, max_val = code(min_val, max_val, board[i])
        # print(min_val, max_val)
    row = max_val
    min_val, max_val = 0, 7
    for i in range(7, 10):
        min_val, max_val = code(min_val, max_val, board[i])
    col = max_val
    SeatID = 8 * row + col
    print('row: ', row, 'col: ', col,'SeatID: ', SeatID)
    all_seats.append(SeatID)
highest_ID = max(all_seats)
print('highest_ID: ', highest_ID)
print('my seat ID is within is : ', [i+1 for i in all_seats if i+1 not in all_seats])
