import math
import time
from functools import cache


@cache
def apply(stone, count):
    if not count:
        return 1
    if stone == 0:
        return apply(1, count - 1)
    digits = math.floor(math.log10(stone)) + 1
    if not digits & 1:
        pow10 = 10 ** (digits // 2)
        return apply(stone // pow10, count - 1) + apply(stone % pow10, count - 1)
    return apply(stone * 2024, count - 1)


def part1(src, count=25):
    return sum(apply(stone, count) for stone in tuple(map(int, src.split())))


def part2(src):
    return part1(src, 75)


SAMPLE = "125 17"

assert part1(SAMPLE) == 55312

with open('in/11.txt', 'rt') as f:
    data = f.read()

print(part1(data))
start = time.time()
print(part2(data))
print(time.time() - start)
