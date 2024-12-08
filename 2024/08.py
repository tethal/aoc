import itertools
import time
from collections import defaultdict

from util import Vector


def parse(src):
    antennas = defaultdict(list)
    max_x = 0
    max_y = 0
    for y, line in enumerate(src.splitlines()):
        for x, c in enumerate(line):
            if c != '.':
                antennas[c].append(Vector(x, y))
            max_x = max(max_x, x)
        max_y = max(max_y, y)
    return antennas, max_x, max_y


def common(src, scalar_generator):
    antennas, max_x, max_y = parse(src)
    result = set()
    for l in antennas.values():
        for a, b in itertools.combinations(l, 2):
            for i in scalar_generator():
                v = a + (b - a) * i
                if 0 <= v.x <= max_x and 0 <= v.y <= max_y:
                    result.add(v)
    return len(result)


def part1(src):
    return common(src, lambda: (-1, 2))


def part2(src):
    return common(src, lambda: range(-60, 60))


SAMPLE = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

assert part1(SAMPLE) == 14
assert part2(SAMPLE) == 34

with open('in/08.txt', 'rt') as f:
    data = f.read()

print(part1(data))
start = time.time()
print(part2(data))
print(time.time() - start)
