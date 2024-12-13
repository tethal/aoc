import re
import time

RE = re.compile("Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)")


def determinant(a, b, c, d):
    return a * d - b * c


def solve(ax, ay, bx, by, kx, ky, add=0):
    d = determinant(ax, bx, ay, by)
    if not d:
        return None
    a = determinant(kx + add, bx, ky + add, by) / d
    b = determinant(ax, kx + add, ay, ky + add) / d
    return 3 * int(a) + int(b) if a.is_integer() and b.is_integer() else None


def part1(src):
    return sum(filter(lambda v: v is not None, (solve(*map(int, s)) for s in RE.findall(src))))


def part2(src):
    return sum(filter(lambda v: v is not None, (solve(*map(int, s), add=10000000000000) for s in RE.findall(src))))


SAMPLE = """\
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

assert part1(SAMPLE) == 480

with open('in/13.txt', 'rt') as f:
    data = f.read()

print(part1(data))
start = time.time()
print(part2(data))
print(time.time() - start)
