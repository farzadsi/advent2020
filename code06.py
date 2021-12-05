import os
import re


cdir = os.path.dirname(__file__)
os.chdir(cdir)
os.getcwd()

count = 0
with open("data06") as file:
    data = file.read()

data = data.split('\n\n')

for c_group in data:
    indivs = c_group.splitlines()
    ref = set(indivs[0])
    if len(indivs)>1:
        for indiv in indivs[1:]:
            ref = ref.intersection(set(indiv))
    # print(len(ref))
    count += len(ref)

print('count= ', count)
