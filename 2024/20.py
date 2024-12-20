import time

from util import E, N, S, Vector, W


def common(src, max_cheat, min_save=100):
    grid = {}
    for y, line in enumerate(src.splitlines()):
        for x, char in enumerate(line):
            if char == 'S':
                pos = Vector(x, y)
            if char == 'E':
                end = Vector(x, y)
            grid[Vector(x, y)] = '#' if char == '#' else '.'

    distances = {pos: 0}
    while pos != end:
        for d in N, S, W, E:
            npos = pos + d
            if grid[npos] == '.' and npos not in distances:
                distances[npos] = distances[pos] + 1
                pos = npos
                break

    result = 0
    for v0, c in grid.items():
        if c == '#':
            continue
        v0d = distances[v0]
        for y in range(-max_cheat, max_cheat + 1):
            for x in range(-max_cheat, max_cheat + 1):
                hdist = abs(x) + abs(y)
                if hdist < max_cheat + 1 and distances.get(Vector(x + v0.x, y + v0.y), -1) - v0d - hdist >= min_save:
                    result += 1

    return result


def part1(src, min_save=100):
    return common(src, 2, min_save)


def part2(src, min_save=100):
    return common(src, 20, min_save)


SAMPLE = """\
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""

assert part1(SAMPLE, 40) == 2
assert part2(SAMPLE, 70) == 41

with open('in/20.txt', 'rt') as f:
    data = f.read()

print(part1(data))
start = time.time()
print(part2(data))
print(time.time() - start)
