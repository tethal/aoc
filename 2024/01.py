def parse(src):
    return tuple(zip(*list(map(int, line.split("   ")) for line in src.splitlines())))

def part1(src):
    left, right = parse(src)
    return sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))


def part2(src):
    left, right = parse(src)
    return sum(a * right.count(a) for a in left)

SAMPLE = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""

assert part1(SAMPLE) == 11
assert part2(SAMPLE) == 31

with open('in/01.txt', 'rt') as f:
    data = f.read()

print(part1(data))
print(part2(data))
