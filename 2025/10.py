import re
from functools import reduce
from itertools import chain, combinations
from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np

RE = re.compile(r'\[(.*)\] (.*) {(.*)}')

def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def parse(src, part2=False):
    def parse_line(line):
        lights, buttons, joltages = RE.fullmatch(line).groups()
        lights = reduce(lambda acc, p: acc | ((1 << p[0]) if p[1] == '#' else 0), enumerate(lights), 0)
        buttons = [reduce(lambda acc, v: acc | 1 << int(v), b[1:-1].split(','), 0) for b in buttons.split(' ')]
        joltages = tuple(map(int, joltages.split(',')))
        if part2:
            l = len(joltages)
            buttons = tuple(tuple(map(int, reversed((("0" * l) + (bin(v)[2:]))[-l:]))) for v in buttons)
        return lights, buttons, joltages
    return [parse_line(line) for line in src.splitlines()]


def part1(src):
    machines = parse(src)
    return sum(min(len(p) for p in powerset(buttons) if reduce(lambda acc, v: acc ^ v, p, 0) == lights) for lights, buttons, _ in machines)


def part2(src):
    machines = parse(src, True)

    def solve(buttons, joltages):
        return round(milp(c=np.ones(len(buttons)),
                      constraints=LinearConstraint(np.array(buttons).T, joltages, joltages),
                      integrality=np.ones(len(buttons)),
                      bounds=Bounds(0, np.inf)).fun)

    return sum(solve(buttons, joltages) for _, buttons, joltages in machines)


SAMPLE = """\
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

assert part1(SAMPLE) == 7
assert part2(SAMPLE) == 33

with open('in/10.txt', 'rt') as f:
    data = f.read()

print(part1(data))
print(part2(data))
