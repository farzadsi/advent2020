import os

cdir = os.path.dirname(__file__)
os.chdir(cdir)
os.getcwd()

with open("data10") as file:
    data = file.read().split('\n')

data = [int(i) for i in data]

full_seq = data.copy()
full_seq.append(0)
full_seq.append(max(full_seq) + 3)
full_seq.sort()

jolts = [full_seq[n + 1] - i for n, i in enumerate(full_seq[:-1])]
print('number of 1-jolt: ', jolts.count(1), '|| number of 3-jolt: ', jolts.count(3),
      '==> product: ', jolts.count(1)*jolts.count(3))
count = 0
second = 0
n = 0
combinations = {1:1, 2:2, 3:4, 4:7}
total = 1
while n < len(jolts):
    jol = jolts[n]
    if jol == 1:
        cont_1 = 1
        n += 1
        while jolts[n] == 1:
            n += 1
            cont_1 += 1
        print(cont_1, combinations[cont_1])
        total *= combinations[cont_1]
    else:
        n += 1

print(total)
