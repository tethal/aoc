import math
import re
from itertools import groupby


def part1(src):
    return sum({'*': math.prod, '+': sum}[row[-1]](map(int, row[:-1])) for row in zip(*[re.split(r'\s+', l.strip()) for l in  src.splitlines()]))


def part2(src):
    *data, ops = src.splitlines()
    return sum({'*': math.prod, '+': sum}[op](map(int, g)) for g, op in zip((g for a, g in groupby([''.join(r) for r in (zip(*data))], lambda s: bool(s.strip())) if a), re.split(r'\s+', ops)))


SAMPLE = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + """

assert part1(SAMPLE) == 4277556
assert part2(SAMPLE) == 3263827

with open('in/06.txt', 'rt') as f:
    data = f.read()

print(part1(data))
print(part2(data))
