import re

def solve(src, regex):
    result = 0
    for r in src.strip().split(','):
        a, b = r.split('-')
        for i in range(int(a), int(b) + 1):
            if re.fullmatch(regex, str(i)):
                result += i
    return result

def part1(src):
    return solve(src, r"(\d+?)\1")


def part2(src):
    return solve(src, r"(\d+?)(\1)+")

SAMPLE = """\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
"""

assert part1(SAMPLE) == 1227775554
assert part2(SAMPLE) == 4174379265

with open('in/02.txt', 'rt') as f:
    data = f.read()

print(part1(data))
print(part2(data))
