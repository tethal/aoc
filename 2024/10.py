import time
from collections import defaultdict

from util import E, N, S, Vector, W


def common(src, collection, appender):
    grid = {Vector(x, y): int(c) for y, row in enumerate(src.splitlines()) for x, c in enumerate(row)}
    trails = defaultdict(collection)

    def visit(pos, height, start_pos):
        if height == 9:
            appender(trails[start_pos], pos)
        for direction in (N, S, W, E):
            new_pos = pos + direction
            if grid.get(new_pos, None) == height + 1:
                visit(new_pos, height + 1, start_pos)

    for v, c in grid.items():
        if c == 0:
            visit(v, 0, v)
    return sum(len(x) for x in trails.values())


def part1(src):
    return common(src, set, set.add)


def part2(src):
    return common(src, list, list.append)


SAMPLE = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

assert part1(SAMPLE) == 36
assert part2(SAMPLE) == 81

with open('in/10.txt', 'rt') as f:
    data = f.read()

print(part1(data))
start = time.time()
print(part2(data))
print(time.time() - start)
