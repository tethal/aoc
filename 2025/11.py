import re
from functools import reduce, lru_cache
from itertools import chain, combinations
from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np


def parse(src):
    return {l.split(':')[0] : set(l.split(': ')[1].split()) for l in src.splitlines()}


def part1(src):
    data = parse(src)
    @lru_cache
    def count_paths(start):
        if start == 'out':
            return 1
        return sum(count_paths(d) for d in data[start])
    return count_paths('you')


def part2(src):
    data = parse(src)
    @lru_cache
    def count_paths(start, dac, fft):
        if start == 'out':
            return dac and fft
        return sum(count_paths(d, dac or start=='dac', fft or start=='fft') for d in data[start])
    return count_paths('svr', False, False)


SAMPLE = """\
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

SAMPLE2 = """\
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""

assert part1(SAMPLE) == 5
assert part2(SAMPLE2) == 2

with open('in/11.txt', 'rt') as f:
    data = f.read()

print(part1(data))
print(part2(data))
