import os
import re
import pandas as pd

cdir = os.path.dirname(__file__)
os.chdir(cdir)
os.getcwd()

with open("data08") as file:
    data = file.read().split('\n')

df = pd.DataFrame(columns=['instruction', 'opt', 'value', 'num_run'])

p = re.compile(r'([a-zA-Z]{3}) ([-+]?)(\d*)')
st_data = list()
for line in data:
    st_data.append({'instruction': p.search(line)[1],
    'opt': p.search(line)[2],
    'value': p.search(line)[3],
    'num_run': 0})
df = pd.DataFrame(st_data)


def plut_minus(value, val, opt):
    val = int(val)
    if opt == '+':
        value += val
    elif opt == '-':
        value -= val
    return value

def test_df(df):
    idx = 0
    accumulator = 0
    while True:
        if idx >= len(df):
            return accumulator, 1
        # print(idx)
        inst, opt, val, num_run = df.iloc[idx]
        if num_run == 1:
            return accumulator, 0
        else:
            df.at[idx, 'num_run'] = 1
        # apply rules
        if inst == 'nop':
            idx += 1
        elif inst == 'jmp':
            idx = plut_minus(idx, val, opt)
        elif inst == 'acc':
            idx += 1
            accumulator = plut_minus(accumulator, val, opt)


replacing_dic = {'jmp': 'nop',
                 'nop': 'jmp'}
success = 0
for df_idx, c_row in df.iterrows():
    if c_row.instruction in ['jmp', 'nop']:
        print(df_idx)
        new_df = df.copy()
        new_df.at[df_idx, 'instruction'] = replacing_dic[c_row.instruction]
        accumulator, success = test_df(new_df)
        if success:
            print('accumulator of correct set: ', accumulator)
            break