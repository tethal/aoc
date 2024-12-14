import re
import time
from collections import defaultdict

RE = re.compile("p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")


def sign(n):
    return -1 if n < 0 else 1 if n > 0 else 0


def part1(src, w=101, h=103):
    r = defaultdict(int)
    for line in RE.findall(src):
        px, py, vx, vy = map(int, line)
        for i in range(100):
            px = (px + vx) % w
            py = (py + vy) % h
        qx = sign(px - w // 2)
        qy = sign(py - h // 2)
        r[qx, qy] += 1
    return r[-1, -1] * r[-1, 1] * r[1, -1] * r[1, 1]


def part2(src, w=101, h=103):
    robots = []
    for line in RE.findall(src):
        px, py, vx, vy = map(int, line)
        robots.append([px, py, vx, vy])

    for i in range(10000):
        r = [[0] * w for _ in range(h)]
        for robot in robots:
            px, py, vx, vy = robot
            px = (px + vx) % w
            py = (py + vy) % h
            robot[0] = px
            robot[1] = py
            r[py][px] += 1
        if i % 103 == 57:  # constants determined experimentally
            print(i + 1)
            for y in range(h):
                for x in range(w):
                    print('*' if r[y][x] else '.', end='')
                print()


SAMPLE = """\
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""

assert part1(SAMPLE, 11, 7) == 12

with open('in/14.txt', 'rt') as f:
    data = f.read()

print(part1(data))
start = time.time()
print(part2(data))
print(time.time() - start)
