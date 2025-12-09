from itertools import chain, combinations, pairwise

def area(a, b):
    return (abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1)

def part1(src):
    data = [tuple(map(int, l.split(','))) for l in src.splitlines()]
    return max(area(a, b) for a, b in combinations(data, 2))


def part2(src):
    data = [tuple(map(int, l.split(','))) for l in src.splitlines()]

    def intersects(a, b, p1, p2):
        (ax, bx), (ay, by) = map(sorted, zip(a, b))
        (x1, x2), (y1, y2) = map(sorted, zip(p1, p2))
        return ax < x2 and bx > x1 and ay < y2 and by > y1

    return max(area(a, b) for a, b in combinations(data, 2) if not any(intersects(a, b, p1, p2) for p1, p2 in pairwise(chain(data, [data[0]]))))


SAMPLE = """\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

assert part1(SAMPLE) == 50
assert part2(SAMPLE) == 24

with open('in/09.txt', 'rt') as f:
    data = f.read()

print(part1(data))
print(part2(data))
