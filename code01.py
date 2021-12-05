import os
import re


cdir = os.path.dirname(__file__)
os.chdir(cdir)
os.getcwd()

with open("code02") as file:
    data = file.read().splitlines()

# structure of each line {min#}-{max#} {char}: {pwd}
p = re.compile(r'(\d*)-(\d*)\s(\w*):\s(\w*)')
counter = 0
for i in data:
    # print(i)
    min_num, max_num, chr, pwd = p.match(i).groups()
    min_num, max_num = int(min_num)-1, int(max_num)-1
    # test = re.compile(chr)
    if len(pwd) < max_num:
        print('password smaller than max number')
    if (pwd[min_num] == chr) != (pwd[max_num] == chr):
        counter += 1
        print(chr, min_num, max_num, pwd)
print('number of valid passwords', counter)

