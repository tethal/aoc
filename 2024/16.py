import time

from util import E, N, S, TURN_LEFT, TURN_RIGHT, Vector, W


def common(src):
    queue = []
    grid = {}
    for y, row in enumerate(src.splitlines()):
        for x, c in enumerate(row):
            v = Vector(x, y)
            if c == 'S':
                queue.append((v, E, 0, (None, None)))
            if c == 'E':
                target = v
            grid[v] = '#' if c == '#' else '.'
    visited = {}
    while queue:
        pos, d, score, came_from = queue.pop(0)
        if (pos, d) in visited:
            min_score, cf = visited[(pos, d)]
            if min_score == score:
                cf.add(came_from)
            if min_score <= score:
                continue
        visited[(pos, d)] = (score, {came_from})
        if grid[pos + d] == '.':
            queue.append((pos + d, d, score + 1, (pos, d)))
        queue.append((pos, TURN_RIGHT[d], score + 1000, (pos, d)))
        queue.append((pos, TURN_LEFT[d], score + 1000, (pos, d)))
    return visited, target


def part1(src):
    visited, target = common(src)
    return min(*(visited[(target, d)][0] for d in (W, S, E, N)))


def part2(src):
    visited, target = common(src)
    on_path = {target}
    queue = []
    m = min(*(visited[(target, d)][0] for d in (W, S, E, N)))
    for d in (W, S, E, N):
        score, cf = visited[(target, d)]
        if score == m:
            queue.extend(cf)

    while queue:
        v, d = queue.pop(0)
        if v is None:
            continue
        on_path.add(v)
        queue.extend(visited[(v, d)][1])

    return len(on_path)


SAMPLE = """\
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

SAMPLE2 = """\
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""

assert part1(SAMPLE) == 7036
assert part1(SAMPLE2) == 11048
assert part2(SAMPLE) == 45
assert part2(SAMPLE2) == 64

with open('in/16.txt', 'rt') as f:
    data = f.read()

print(part1(data))
start = time.time()
print(part2(data))
print(time.time() - start)
