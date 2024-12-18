import heapq
import time
from bisect import bisect_left
from itertools import count

from util import E, N, S, Vector, W


def parse(src):
    return [Vector(int(line.split(',')[0]), int(line.split(',')[1])) for line in src.splitlines()]


def find_path(coords, size, cnt):
    grid = {v for v in coords[:cnt]}
    cntr = count()  # makes tuples in queue comparable
    queue = [(0, next(cntr), Vector(0, 0))]
    visited = {Vector(0, 0): 0}
    while queue:
        t, _, pos = heapq.heappop(queue)
        visited[pos] = t
        if pos.x == size - 1 and pos.y == size - 1:
            return t
        for d in N, S, W, E:
            npos = pos + d
            if 0 <= npos.x < size and 0 <= npos.y < size and npos not in grid and visited.get(npos, t + 2) > t + 1:
                visited[npos] = t + 1
                heapq.heappush(queue, (t + 1, next(cntr), npos))
    return None


def part1(src, size=71, cnt=1024):
    return find_path(parse(src), size, cnt)


def part2(src, size=71):
    coords = parse(src)
    v = coords[bisect_left(list(range(len(coords))), True, key=lambda i: find_path(coords, size, i + 1) is None)]
    return f'{v.x},{v.y}'


SAMPLE = """\
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""

assert part1(SAMPLE, 7, 12) == 22
assert part2(SAMPLE, 7) == '6,1'

with open('in/18.txt', 'rt') as f:
    data = f.read()

print(part1(data))
start = time.time()
print(part2(data))
print(time.time() - start)
