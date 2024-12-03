import re

def part1(src):
    regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    return sum(int(a) * int(b) for a, b in regex.findall(src))

def part2(src):
    regex = re.compile(r"(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))")
    enabled = True
    result = 0
    for match in regex.finditer(src):
        if match.group(4):
            enabled = True
        elif match.group(5):
            enabled = False
        elif enabled:
            a, b = map(int, match.groups()[1:3])
            result += a * b
    return result

SAMPLE = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
SAMPLE2 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
assert part1(SAMPLE) == 161
assert part2(SAMPLE2) == 48

with open('in/03.txt', 'rt') as f:
    data = f.read()

print(part1(data))
print(part2(data))
