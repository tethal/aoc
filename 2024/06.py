import time

from util import E, N, S, TURN_RIGHT, Vector, W

D = {'^': N, 'v': S, '<': W, '>': E}


def parse(src):
    m = {}
    for y, line in enumerate(src.splitlines()):
        for x, char in enumerate(line):
            if char in D:
                pos, d = (Vector(x, y), D[char])
                m[Vector(x, y)] = '.'
            else:
                m[Vector(x, y)] = char
    return m, pos, d


def simulate_guard(m, pos, d, obstacle=Vector(-1, -1)):
    visited_dir = set()
    while True:
        if (pos, d) in visited_dir:
            return None  # loop
        visited_dir.add((pos, d))
        new_pos = pos + d
        if new_pos not in m:
            return visited_dir
        if new_pos == obstacle or m[new_pos] == '#':
            d = TURN_RIGHT[d]
        else:
            pos = new_pos


def part1(src):
    m, pos, d = parse(src)
    return len(set(p for p, _ in simulate_guard(m, pos, d)))


def part2(src):
    m, pos, d = parse(src)
    count = 0
    c = 0
    s = time.time()
    for coords, char in m.items():
        if char == '#' or coords == pos:
            continue
        if not simulate_guard(m, pos, d, coords):
            count += 1
        c += 1
        if not (c % 100):
            delta = time.time() - s
            print(delta / (c / len(m)))
    return count


SAMPLE = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

assert part1(SAMPLE) == 41
assert part2(SAMPLE) == 6

with open('in/06.txt', 'rt') as f:
    data = f.read()

print(part1(data))
start = time.time()
print(part2(data))
print(time.time() - start)

# cpython 243s
# graalpy 9.5s
