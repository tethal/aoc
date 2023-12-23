from collections import deque

with open('ex/23.txt', 'rt') as f:
    grid = f.read().splitlines()

w = len(grid[0])
h = len(grid)


def find_intersections():
    s = (grid[0].find('.'), 0)
    e = (grid[-1].find('.'), h - 1)
    result = {s, e}
    for y, r in enumerate(grid[1:-1], start=1):
        for x, c in enumerate(r[1:-1], start=1):
            if c == '#':
                continue
            cnt = sum(1 for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)) if grid[y+dy][x+dx] in ".<>v^")
            if cnt > 2:
                result.add((x, y))
    return s, e, result


def find_neighbours(all_dir_walkable):
    neighbours = {}
    for ix, iy in intersections:
        queue = deque([(ix, iy, 0)])
        visited = set()
        n = []
        while queue:
            x, y, d = queue.popleft()
            visited.add((x, y))
            for nx, ny, a in (x, y + 1, 'v'), (x, y - 1, '^'), (x + 1, y, '>'), (x - 1, y, '<'):
                if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in visited and grid[ny][nx] in all_dir_walkable+a:
                    if (nx, ny) in intersections:
                        n.append((nx, ny, d + 1))
                    else:
                        queue.append((nx, ny, d + 1))
        neighbours[(ix, iy)] = n
    return neighbours


def find_longest(ln, s):
    if s == end:
        return ln
    visited.add(s)
    m = 0
    for x, y, d in neighbours[s]:
        if (x, y) not in visited:
            m = max(m, find_longest(ln + d, (x, y)))
    visited.remove(s)
    return m


start, end, intersections = find_intersections()

visited = set()
neighbours = find_neighbours('.')
print(find_longest(0, start))

visisted = set()
neighbours = find_neighbours('.<>^v')
print(find_longest(0, start))
