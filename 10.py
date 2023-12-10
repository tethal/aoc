
NEIGHBOURS = {
    '|': ((0, -1), (0, 1)),
    '-': ((-1, 0), (1, 0)),
    'L': ((0, -1), (1, 0)),
    'J': ((0, -1), (-1, 0)),
    'F': ((0, 1), (1, 0)),
    '7': ((0, 1), (-1, 0)),
    '.': (),
    'S': ((0, 1), (0, -1), (1, 0), (-1, 0))
}

with open('10a.txt', 'rt') as f:
    maze = f.readlines()

h = len(maze) + 2
w = len(maze[0]) + 1

maze = ['.' * w] + ['.' + row.strip() + '.' for row in maze] + ['.' * w]


def find_start():
    for y in range(h):
        for x in range(w):
            if maze[y][x] == 'S':
                return x, y
    assert False, 'no start'


sx, sy = find_start()


def find_path(x, y):
    visited = [[False] * w for _ in range(h)]
    d = 1
    visited[sy][sx] = True
    frm = (sx, sy)
    while True:
        visited[y][x] = True
        d += 1
        nn = {(x + n[0], y + n[1]) for n in NEIGHBOURS[maze[y][x]]} - {frm}
        if not nn:
            return None, -1
        frm = (x, y)
        x, y = next(iter(nn))
        if (x, y) == (sx, sy):
            return visited, d


border, dist = next((border, dist) for border, dist in [find_path(sx + dx, sy + dy) for dx, dy in NEIGHBOURS['S']] if border)

print(dist // 2)

if border[sy][sx + 1]:
    sr = 'F' if border[sy + 1][sx] else 'L'
else:
    sr = '7' if border[sy + 1][sx] else 'J'

maze = [''.join(sr if x == sx and y == sy else maze[y][x] if border[y][x] else '.' for x in range(w)) for y in range(h)]

cnt = 0
for row in maze:
    inside = False
    for c in row:
        if c in '|FL':
            inside = not inside
            last_corner = c
        elif c == '7' and last_corner == 'F':
            inside = not inside
        elif c == 'J' and last_corner == 'L':
            inside = not inside
        if c == '.' and inside:
            cnt += 1

print(cnt)
