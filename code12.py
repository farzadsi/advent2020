import math
import os
import re
import numpy as np


class Boat:
    def __init__(self):
        self.location = np.array([0, 0])
        self.direction = 'E'
        self._news_dict= {'N': np.array([0, 1]),
                        'E': np.array([1, 0]),
                        'W': np.array([-1, 0]),
                        'S': np.array([0, -1])}
        self._rotation= {'R': -1, 'L': 1}
        self._geo_degree = {'E': 0, 'W': 180, 'N': 90, 'S': 270}
        self._degree_geo = {0: 'E', 180: 'W', 90: 'N', 270: 'S'}

    def move(self, step):
        self._newslrf = step[0]
        self._nstep = step[1]

        if self._newslrf == 'F':
            self._newslrf = self.direction
            self._update_location(step)
        elif step[0] in self._news_dict.keys():
            self._update_location(step)
        elif step[0] in self._rotation.keys():
            self._update_direction(step)

    def _update_location(self, step):
        self.location += self._news_dict[self._newslrf] * self._nstep

    def _update_direction(self, step):
        self.new_degree = self._geo_degree[self.direction] + self._rotation[self._newslrf] * self._nstep
        self.new_degree = (self.new_degree + 360) % 360
        self.direction = self._degree_geo[self.new_degree]


class Boat_wp:
    def __init__(self):
        self.location = np.array(([0], [0]))
        self.wp_location = np.array(([10], [1]))
        self._news_dict= {'N': np.array(([0], [1])),
                        'E': np.array(([1], [0])),
                        'W': np.array(([-1], [0])),
                        'S': np.array(([0], [-1]))}
        self._rotation= {'R': -1, 'L': 1}


    def move(self, step):
        self._newslrf = step[0]
        self._nstep = step[1]

        if self._newslrf == 'F':
            self._update_location()
        elif step[0] in self._news_dict.keys():
            self._update_wp_location()
        elif step[0] in self._rotation.keys():
            self._update_wp_direction()

    def _update_location(self):
        self.location += self.wp_location * self._nstep

    def _update_wp_location(self):
        self.wp_location += self._news_dict[self._newslrf] * self._nstep

    def _update_wp_direction(self):
        self._nstep = math.radians(self._rotation[self._newslrf] * self._nstep)
        self._matrix_rotation = np.int64(np.array(([math.cos(self._nstep), -math.sin(self._nstep)],
                                          [math.sin(self._nstep), math.cos(self._nstep)])))
        self.wp_location = np.matmul(self._matrix_rotation, self.wp_location)


cdir = os.path.dirname(__file__)
os.chdir(cdir)
os.getcwd()

p = re.compile('([A-Z])(\d*)')

with open("data12") as file:
    data = file.read().split('\n')

data = [[p.search(t)[1], int(p.search(t)[2])] for t in data]
data2 = list()

boat = Boat_wp()

for line in data:
    boat.move(line)

print(boat.location)
print('Manhatan Distance: ', abs((boat.location)).sum())