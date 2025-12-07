import math
import re
from functools import lru_cache
from itertools import groupby


def part1(src):
    data = [list(l) for l in src.splitlines()]
    split_count = 0
    for prev, row in zip(data, data[1:]):
        for x, c in enumerate(prev):
            if c in 'S|':
                if row[x] == '^':
                    split_count += 1
                    row[x-1] = '|'
                    row[x+1] = '|'
                else:
                    row[x] = '|'
    return split_count


def part2(src):
    data = [list(l) for l in src.splitlines()]

    @lru_cache
    def solve(col, row):
        if row >= len(data):
            return 1
        if data[row][col] == '^':
            return solve(col - 1, row) + solve(col + 1, row)
        else:
            return solve(col, row + 1)

    return solve(data[0].index('S'), 1)


SAMPLE = """\
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""

assert part1(SAMPLE) == 21
assert part2(SAMPLE) == 40

with open('in/07.txt', 'rt') as f:
    data = f.read()

print(part1(data))
print(part2(data))
