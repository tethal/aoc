import re

def max_joltage(line, battery_count):
    r = ""
    for i in range(-battery_count + 1, 1):
        new_digit = max(line[:i] if i else line)
        r += new_digit
        line = line[line.index(new_digit) + 1:]
    return int(r)


def part1(src):
    return sum(max_joltage(line, 2) for line in src.splitlines())


def part2(src):
    return sum(max_joltage(line, 12) for line in src.splitlines())

SAMPLE = """\
987654321111111
811111111111119
234234234234278
818181911112111
"""

assert part1(SAMPLE) == 357
assert part2(SAMPLE) == 3121910778619

with open('in/03.txt', 'rt') as f:
    data = f.read()

print(part1(data))
print(part2(data))
