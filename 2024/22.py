import time
from collections import defaultdict


def gen(s):
    s = (s ^ (s << 6)) & 16777215
    s = (s ^ (s >> 5)) & 16777215
    s = (s ^ (s << 11)) & 16777215
    return s


def part1(src):
    def gen2000(x):
        for i in range(2000):
            x = gen(x)
        return x

    return sum(gen2000(n) for n in map(int, src.splitlines()))


def part2(src):
    sums = defaultdict(int)
    for x in map(int, src.splitlines()):
        seen = set()
        seq = 0, 0, 0, 0
        for i in range(2000):
            y = gen(x)
            seq = seq[1], seq[2], seq[3], (y % 10) - (x % 10)
            x = y
            if i >= 3 and seq not in seen:
                seen.add(seq)
                sums[seq] += y % 10
    return max(sums.values())


SAMPLE = """\
1
10
100
2024
"""

SAMPLE2 = """\
1
2
3
2024
"""

assert part1(SAMPLE) == 37327623
assert part2(SAMPLE2) == 23

with open('in/22.txt', 'rt') as f:
    data = f.read()

print(part1(data))
start = time.time()
print(part2(data))
print(time.time() - start)
