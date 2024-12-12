import time
from collections import defaultdict

from util import E, N, S, Vector, W


def visit(v, c, grid, visited, perimeter):
    if v in visited:
        return 0
    assert grid.get(v) == c
    visited.add(v)
    area = 1
    for d in N, S, W, E:
        v1 = v + d
        if grid.get(v1, None) == c:
            area += visit(v1, c, grid, visited, perimeter)
        else:
            perimeter.add((v.x, v.y, d))
    return area


def part1(src):
    grid = {Vector(x, y): c for y, row in enumerate(src.splitlines()) for x, c in enumerate(row)}
    visited = set()

    result = 0
    for v, c in grid.items():
        perimeter = set()
        area = visit(v, c, grid, visited, perimeter)
        result += area * len(perimeter)

    return result


def count_sequences(numbers):
    number_of_sequences = 0
    numbers.sort()
    last_value = -100
    for value in numbers:
        if value != last_value + 1:
            number_of_sequences += 1
        last_value = value
    return number_of_sequences


def count_sides(perimeter):
    side_coords = {d: defaultdict(list) for d in (N, S, W, E)}

    for x, y, d in perimeter:
        if d in (N, S):
            side_coords[d][y].append(x)
        else:
            side_coords[d][x].append(y)

    return sum(count_sequences(numbers) for s in side_coords.values() for numbers in s.values())


def part2(src):
    grid = {Vector(x, y): c for y, row in enumerate(src.splitlines()) for x, c in enumerate(row)}
    visited = set()

    result = 0
    for v, c in grid.items():
        perimeter = set()
        area = visit(v, c, grid, visited, perimeter)
        result += area * count_sides(perimeter)

    return result


SAMPLE = """\
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

assert part1(SAMPLE) == 1930
assert part2(SAMPLE) == 1206

with open('in/12.txt', 'rt') as f:
    data = f.read()

print(part1(data))
start = time.time()
print(part2(data))
print(time.time() - start)
