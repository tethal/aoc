from collections import deque

TABLE = {
    r'.W': 'W',
    r'.N': 'N',
    r'.E': 'E',
    r'.S': 'S',
    r'/E': 'N',
    r'/W': 'S',
    r'/N': 'E',
    r'/S': 'W',
    r'\W': 'N',
    r'\E': 'S',
    r'\N': 'W',
    r'\S': 'E',
    r'|S': 'S',
    r'|N': 'N',
    r'|E': 'NS',
    r'|W': 'NS',
    r'-S': 'WE',
    r'-N': 'WE',
    r'-E': 'E',
    r'-W': 'W',
}

DIRS = {
    'W': (-1, 0),
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
}


def beams(data, ix, iy, idir):
    queue = deque(((ix, iy, idir), ))
    visited_from = [[set() for _ in range(len(data[0]))] for _ in range(len(data))]
    while queue:
        x, y, d = queue.popleft()
        if not (0 <= y < len(data) and 0 <= x < len(data[0])) or d in visited_from[y][x]:
            continue
        visited_from[y][x].add(d)
        for new_dir in TABLE[data[y][x] + d]:
            dx, dy = DIRS[new_dir]
            queue.append((x + dx, y + dy, new_dir))
    return sum(1 if len(v) else 0 for r in visited_from for v in r)


with open('in/16.txt', 'rt') as f:
    src = f.read().splitlines()

print(beams(src, 0, 0, 'E'))

m = 0
for y in range(len(src)):
    m = max(m, beams(src, 0, y, 'E'))
    m = max(m, beams(src, len(src[0]) - 1, y, 'W'))

for x in range(len(src[0])):
    m = max(m, beams(src, x, 0, 'S'))
    m = max(m, beams(src, x, len(src) - 1, 'N'))

print(m)
