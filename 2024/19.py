import time
from functools import cache


@cache
def options(design, patterns):
    if not design:
        return 1
    return sum(options(design[len(pattern):], patterns) for pattern in patterns if design.startswith(pattern))


def common(src):
    patterns, designs = src.split('\n\n')
    patterns = tuple(patterns.split(', '))
    return map(lambda d: options(d, patterns), designs.splitlines())


def part1(src):
    return sum(1 for x in common(src) if x)


def part2(src):
    return sum(common(src))


SAMPLE = """\
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""

assert part1(SAMPLE) == 6
assert part2(SAMPLE) == 16

with open('in/19.txt', 'rt') as f:
    data = f.read()

print(part1(data))
start = time.time()
print(part2(data))
print(time.time() - start)
