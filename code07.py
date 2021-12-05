import os
import re


cdir = os.path.dirname(__file__)
os.chdir(cdir)
os.getcwd()

count = 0
with open("data07") as file:
    data = file.readlines()


class Bag:
    def __init__(self, line):
        self.name, self.content = self._line_to_dict(line)

    def can_fit(self, new_bag_name):
        if new_bag_name in list(self.content.keys()):
            return 1
        else:
            return 0

    def _get_content(self, text):
        content = dict()
        # strucutre of content # {color} bag , # {color} bag
        p = re.compile(r'([0-9]*) ([a-zA-Z\x20]*) bag')
        text = text.split(', ')
        for subtext in text:
            content[p.search(subtext)[2]] = int(p.search(subtext)[1]) if subtext != 'no other bags' else 0
        return content


    def _line_to_dict(self, line):
        line_rule = dict()
        # structure of each line {color} ' bags contain ' {subinfo}'
        p = re.compile(r'([a-zA-Z\x20]*) bags contain (.*)(.)')
        bag_name = p.search(line)[1]
        bag_content = self._get_content(p.search(line)[2])
        return bag_name, bag_content


def list_of_bags(input_bag, bags: list):
    list_bags = [target_bag.name for target_bag in bags if target_bag.can_fit(input_bag)]
    return list_bags


def merge_sum_dict(x, y):
    z = {}
    overlapping_keys = x.keys() & y.keys()
    for key in overlapping_keys:
        z[key] = x[key] + y[key]
    for key in x.keys() - overlapping_keys:
        z[key] = x[key]
    for key in y.keys() - overlapping_keys:
        z[key] = y[key]
    return z

bags = [Bag(i) for i in data]


input_bag = ['shiny gold']

can_contain_gold = list()

rules = {bag.name:bag for bag in bags}


while input_bag:
    current_color = input_bag.pop()
    parent_bags = list_of_bags(current_color, bags)
    # print(current_color)
    for cbag in parent_bags:
        if cbag not in can_contain_gold:
            input_bag.append(cbag)
            can_contain_gold.append(cbag)

target_content = rules['shiny gold'].content

count = 0
final_dict = dict()
while target_content:
    cbag, num = target_content.popitem()
    count += num
    new = rules[cbag].content
    if list(new.values()) == [0]:
        continue
    else:
        new = {n: m*num for n, m in new.items()}
        target_content = merge_sum_dict(target_content, new)

print(len(can_contain_gold))
print('total_count', count)
