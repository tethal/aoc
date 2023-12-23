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
        n = set()
        while queue:
            x, y, d = queue.popleft()
            visited.add((x, y))
            for nx, ny, a in (x, y + 1, 'v'), (x, y - 1, '^'), (x + 1, y, '>'), (x - 1, y, '<'):
                if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in visited and grid[ny][nx] in all_dir_walkable+a:
                    if (nx, ny) in intersections:
                        n.add((nx, ny, d + 1))
                    else:
                        queue.append((nx, ny, d + 1))
        neighbours[(ix, iy)] = n
    return neighbours


def find_longest(neighbours, visited, ln, s, e):
    if s == e:
        return ln
    return max((find_longest(neighbours, visited | {(x, y)}, ln + d, (x, y), e) for x, y, d in neighbours[s] if (x, y) not in visited), default=0)


start, end, intersections = find_intersections()
print(find_longest(find_neighbours('.'), set(), 0, start, end))
print(find_longest(find_neighbours('.<>^v'), set(), 0, start, end))
