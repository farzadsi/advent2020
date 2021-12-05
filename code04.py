import os
import re


cdir = os.path.dirname(__file__)
os.chdir(cdir)
os.getcwd()

def check_height(height):
    if 'cm' in height:
        if 150 <= int(height.split('cm')[0]) <= 193:
            return True
        else:
            return False
    elif 'in' in height:
        if 59 <= int(height.split('in')[0]) <= 76:
            return True
        else:
            return False
    else:
        return False

with open("data04") as file:
    data = file.read().split('\n\n')

# structure of each line {min#}-{max#} {char}: {pwd}
# p = re.compile(r'(\d*)-(\d*)\s(\w*):\s(\w*)')
#  # followed by exactly six characters 0-9 or a-f.
p = re.compile(r'#[0-9a-f]{6}')
pid_digit = re.compile(r'[0-9]{9}')

required_fields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
counter = 0
for line in data:
    line = line.replace('\n', ' ').split(' ')
    line_dic = {n.split(':')[0]: n.split(':')[1] for n in line}
    pwd = [i for i in required_fields if i not in line_dic.keys()]
    if len(pwd) != 0:
        counter += 1
        continue
    elif not (1920 <= int(line_dic['byr']) <= 2002):
        print('birth year is invalid')
        counter += 1
        continue
    elif not (2010 <= int(line_dic['iyr']) <= 2020):
        print('issue year is invalid')
        counter += 1
        continue
    elif not (2020 <= int(line_dic['eyr']) <= 2030):
        print('expiration year is invalid')
        counter += 1
        continue
    elif not check_height(line_dic['hgt']):
        print('height is invalid')
        counter += 1
        continue
    elif not p.search(line_dic['hcl']):
        print('hair-color is invalid')
        counter += 1
        continue
    elif line_dic['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        print('eye-color is invalid')
        counter += 1
        continue
    elif not pid_digit.search(line_dic['pid']):
        print('passport ID is invalid')
        counter += 1

print('number of invalid passports', counter)
print('number of valid passports', len(data) - counter)
