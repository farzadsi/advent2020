import os
import numpy as np


class Rule:
    def __init__(self, line):
        self.name, self._rest = line.split(': ')
        self.conditions = self._get_conditions(self._rest)

    @staticmethod
    def _get_conditions(rest):
        conditions = list()
        rest = rest.split(' or ')
        for cond in rest:
            cond = cond.split('-')
            conditions.append([*range(int(cond[0]), int(cond[1])+1)])
        conditions = [i for n in conditions for i in n]
        return conditions

    def check_rule(self, input_list):
        return all(np.isin(input_list, self.conditions))


def clean_up_ticket(raw_tickets):
    tickets = raw_tickets.split('\n')[1:]
    return np.array([a.split(',') for a in tickets]).astype(int)


def get_valid_tickets(tickets: np.ndarray, l_cond: list) -> [int, list]:
    sum_invalid_values = 0
    out = list()
    for vals in tickets:
        if all(np.isin(vals, l_cond)): # if all values are in all condition it is a valid ticket
            out.append(vals)
        else:
            sum_invalid_values += np.where(~np.isin(vals, l_cond), vals, 0).sum()
    return sum_invalid_values, np.array(out) # pd.DataFrame(out, columns=['col'+str(i) for i in range(len(vals))])


def identify_rule(r_names: dict, rules: list):
    rule_names = [rule.name for rule in rules]
    rule_col_map = dict()
    while len(r_names) > 0:
        n_r_names = r_names.copy()
        for name, val in r_names.items():
            if len(val) == 1:
                rule_col_map[name] = n_r_names.pop(name)[0]
                rule_names.remove(val[0])
            else:
                # val = [v for v in val if v in rule_names]
                n_r_names[name] = [v for v in val if v in rule_names]
        r_names = n_r_names
    return rule_col_map


cdir = os.path.dirname(__file__)
os.chdir(cdir)
os.getcwd()
with open("data16") as file:
    # data = file.read().split('\n')
    data = file.read().split('\n\n')
rules_raw = data[0].split('\n')

your_ticket = data[1]
your_ticket = clean_up_ticket(your_ticket)

others_ticket = data[2]
others_ticket = clean_up_ticket(others_ticket)

rules = [Rule(line) for line in rules_raw]
all_conds = [j for i in rules for j in i.conditions]
all_conds = list(set(all_conds))

inv_vals_sum, others_ticket = get_valid_tickets(others_ticket, all_conds)

# we have to have the number of fields for rules and for ticket values
assert len(rules) == others_ticket.shape[1]
col_names = dict()
for i in range(others_ticket.shape[1]):
    col_names[i] = [rule.name for rule in rules if rule.check_rule(others_ticket[:, i])]

col_names = identify_rule(col_names, rules)

values_multi = 1
for k, v in col_names.items():
    if 'departure' in v:
        values_multi *= your_ticket[:, k][0]

print('sum of invalid values in tickets: ', inv_vals_sum)
print('multiply of Departure values in my tickets: ', values_multi)
