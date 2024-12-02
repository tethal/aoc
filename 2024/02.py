from math import copysign


def parse(src):
    return (tuple(map(int, line.split())) for line in src.splitlines())

def is_safe(report):
    deltas = [a - b for a, b in zip(report, report[1:])]
    monotone = all(copysign(1, d) == copysign(1, deltas[0]) for d in deltas)
    return monotone and all(1 <= abs(d) <= 3 for d in deltas)

def part1(src):
    return sum(1 for report in parse(src) if is_safe(report))

def part2(src):
    return sum(1 for report in parse(src) if any(is_safe(report[:i] + report[i + 1:]) for i in range(len(report))))


SAMPLE = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

assert part1(SAMPLE) == 2
assert part2(SAMPLE) == 4

with open('in/02.txt', 'rt') as f:
    data = f.read()

print(part1(data))
print(part2(data))
