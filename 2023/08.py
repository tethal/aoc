import math
import re

RE = re.compile(r'(\w+) = \((\w+), (\w+)\)')


nodes = {}
with open('ex/08.txt', 'rt') as f:
    ins = f.readline().strip()
    f.readline()
    for line in f:
        m = re.search(RE, line)
        n, l, r = m.groups()
        nodes[n] = {'L': l, 'R': r}


def calc_steps(node):
    steps = 0
    while node[2] != 'Z':
        node = nodes[node][ins[steps % len(ins)]]
        steps += 1
    return steps


print(calc_steps('AAA'))
print(math.lcm(*(calc_steps(n) for n in nodes.keys() if n[2] == 'A')))
