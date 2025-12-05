def parse(src):
    a, b = src.split("\n\n")
    return [range(int(x.split("-")[0]), int(x.split("-")[1]) + 1) for x in a.splitlines()], list(map(int, b.splitlines()))

def part1(src):
    ranges, ids = parse(src)
    return sum(any(i in r for r in ranges) for i in ids)


def part2(src):
    ranges, _ = parse(src)
    changed = True
    while changed:
        changed = False
        for i, r1 in enumerate(ranges):
            for j, r2 in enumerate(ranges):
                if i != j:
                    if r1.start in r2:
                        if r1.stop - 1 in r2:
                            ranges[i] = range(0, 0)
                            changed = True
                        else:
                            ranges[i] = range(r2.stop, r1.stop)
                            changed = True
                    elif r1.stop - 1 in r2:
                        ranges[i] = range(r1.start, r2.start)
                        changed = True
    return sum(r.stop - r.start for r in ranges)


SAMPLE = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

assert part1(SAMPLE) == 3
assert part2(SAMPLE) == 14

with open('in/05.txt', 'rt') as f:
    data = f.read()

print(part1(data))
print(part2(data))
