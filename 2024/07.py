import time


def parse(src):
    return [(int(l.split(': ')[0]), tuple(map(int, l.split(': ')[1].split(' ')))) for l in src.splitlines()]


def part1(src):
    def helper(total, acc, inputs):
        if not inputs:
            return total == acc
        v, *rest = inputs
        return helper(total, acc + v, rest) or helper(total, acc * v, rest)

    x = parse(src)
    return sum(total for total, inputs in parse(src) if helper(total, inputs[0], inputs[1:]))


def part2(src):
    def helper(total, acc, inputs):
        if not inputs:
            return total == acc
        v, *rest = inputs
        return (helper(total, acc + v, rest) or
                helper(total, acc * v, rest) or
                helper(total, int(str(acc) + str(v)), rest))

    return sum(total for total, inputs in parse(src) if helper(total, inputs[0], inputs[1:]))


SAMPLE = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

assert part1(SAMPLE) == 3749
assert part2(SAMPLE) == 11387

with open('in/07.txt', 'rt') as f:
    data = f.read()

print(part1(data))
start = time.time()
print(part2(data))
print(time.time() - start)
