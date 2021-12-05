import os
import numpy as np
import re

cdir = os.path.dirname(__file__)
os.chdir(cdir)
os.getcwd()


def parse_mask(mask):
    descrypt = dict()
    for i, n in enumerate(mask):
        if n.lower() != 'x':
            descrypt[i] = n
    return descrypt, i+1


def update_value(dec_val, pmask, mlength):
    bin_val = bin(dec_val)[2:]
    bin_val = (mlength - len(bin_val)) * '0' + bin_val
    # bin_val.replace(pmask)
    for k, v in pmask.items():
        bin_val = bin_val[0:k] + v + bin_val[k+1:]
    return int(bin_val,2)


def parse_mask_mem(mask):
    decrypt = dict()
    for i, n in enumerate(mask):
        if n.lower() != '0':
            decrypt[i] = n
    return decrypt, i+1


def update_mem_location(mem_dec, pmask, mlength):
    bin_mem = bin(mem_dec)[2:]
    bin_mem = (mlength - len(bin_mem)) * '0' + bin_mem
    ext_mem = list()
    for k, v in pmask.items():
        bin_mem = bin_mem[0:k] + v + bin_mem[k + 1:]
    if 'X' not in bin_mem:
        bin_mem = [bin_mem]
    else:
        ext_mem = [bin_mem]
        for i in range(bin_mem.count('X')):
            init_mem = ext_mem.copy()
            ext_mem = list()
            for c_val in init_mem:
                for k, n in enumerate(c_val):
                    if n == 'X':
                        for m in ['0', '1']:
                            ext_mem.append(c_val[0:k] + m + c_val[k + 1:])
                        break

    # [int(mem_val,2) for mem_val in ext_mem]
    return [str(int(mem_val, 2)) for mem_val in ext_mem]


with open("data14") as file:
    data = file.read().split('\n')

part = 2

p = re.compile('mem\[([0-9]*)\] = ([0-9]*)')

cmemory = dict()

for line in data:
    if 'mask' in line:
        c_mask = line.split('mask = ')[1]
        if part == 1:
            c_parsed_mask, mask_length = parse_mask(c_mask)
        if part == 2:
            c_parsed_mask_mem, mask_length = parse_mask_mem(c_mask)
    else:
        mem_input = dict()
        val_to_mem = p.search(line)[2]
        mem_location = p.search(line)[1]
        mem_input[p.search(line)[1]] = p.search(line)[2]
        if part == 1:
            cmemory[mem_location] = update_value(int(val_to_mem), c_parsed_mask, mask_length)
        if part == 2:
            memory_locs = update_mem_location(int(mem_location), c_parsed_mask_mem, mask_length)
            for mloc in memory_locs:
                cmemory[mloc] = int(val_to_mem)

total = 0     # mem_loc_input = {p.search(i)[1]:p.search(i)[2] for i in data[1:]}
for _, val in cmemory.items():
    total += val

print(total)
print('done')