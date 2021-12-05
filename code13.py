import os

import numpy as np

cdir = os.path.dirname(__file__)
os.chdir(cdir)
os.getcwd()


with open("data13") as file:
    data = file.read().split('\n')

my_time = int(data[0])
buses = data[1].split(',')
buses = np.array([int(n) for n in buses if n != 'x'])
residuals = (buses - my_time % buses) % buses
idx = np.argmin(residuals)
print(buses[idx]*min(residuals))


buses = data[1].split(',')
buses = [(int(n), i) for i, n in enumerate(buses) if n != 'x']

base = buses[0]
target = buses[1]


def check_multi(bus1, bus2):
    i = 1
    while True:
        if (bus1[0] * i) % bus2[0] == bus2[0] - bus2[1]:
            # print(bus1[0] * i, bus1[0] * bus2[0])
            return bus1[0] * i, bus1[0] * bus2[0]
        i += 1


def check_next(prev_interval, multi, next_bus):
    i = 0
    while True:
        if (prev_interval + multi * i) % next_bus[0] == next_bus[0] - (next_bus[1] % next_bus[0]):
            new_interval = prev_interval + multi * i
            new_multi = multi * next_bus[0]
            return new_interval, new_multi
        i += 1


interval, multip = check_multi(buses[0], buses[1])

for bus in buses[2:]:
    interval, multip = check_next(interval, multip, next_bus=bus)
    print(interval, multip)


print('multip= ', multip, 'interval= ', interval, 'plus: ', multip+interval)
