from itertools import product, takewhile


def parse(src):
    lines = src.splitlines()
    return [['.'] * (2 + len(lines[0]))] + [list(f".{l}.") for l in lines] + [['.'] * (2 + len(lines[0]))]


def remove_all(grid):
    while True:
        new_grid = [['.' if c == '@' and sum(1 for dy, dx in product(range(-1, 2), repeat=2) if grid[y + dy][x + dx] == '@') <= 4 else c for x, c in enumerate(line)] for y, line in enumerate(grid)]
        yield new_grid, sum(1 for o, n in zip(grid, new_grid) for oo, nn in zip(o, n) if oo != nn)
        grid = new_grid


def part1(src):
    return next(remove_all(parse(src)))[1]


def part2(src):
    return sum(count for grid, count in takewhile(lambda p: p[1], remove_all(parse(src))))


SAMPLE = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

assert part1(SAMPLE) == 13
assert part2(SAMPLE) == 43

with open('in/04.txt', 'rt') as f:
    data = f.read()

print(part1(data))
print(part2(data))
