def parse(src):
    return [int(l[1:]) if l[0] == 'R' else -int(l[1:]) for l in src.splitlines()]

def part1(src):
    value = 50
    result = 0
    for r in parse(src):
        value = (value + r) % 100
        if value == 0:
            result += 1
    return result

def part2(src):
    value = 50
    result = 0
    for r in parse(src):
        v1 = value + r
        if r > 0:
            result += v1 // 100
        else:
            result += -v1 // 100
            if value:
                result += 1
        value = v1 % 100
    return result


SAMPLE = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

assert part1(SAMPLE) == 3
assert part2(SAMPLE) == 6

with open('in/01.txt', 'rt') as f:
    data = f.read()

print(part1(data))
print(part2(data))
