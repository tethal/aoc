import time
from itertools import product


def parse_block(block):
    result = []
    for c in range(len(block[0])):
        r = 0
        while r + 1 < len(block) and block[r + 1][c] == '#':
            r += 1
        result.append(r)
    return result


def part1(src):
    keys = []
    locks = []
    for block in src.split('\n\n'):
        if block[0] == '#':
            locks.append(parse_block(block.splitlines()))
        else:
            keys.append(parse_block(list(reversed(block.splitlines()))))
    return sum(1 for lock, key in product(locks, keys) if all(k + l < 6 for k, l in zip(key, lock)))


SAMPLE = """\
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""

assert part1(SAMPLE) == 3

with open('in/25.txt', 'rt') as f:
    data = f.read()

start = time.time()
print(part1(data))
print(time.time() - start)
