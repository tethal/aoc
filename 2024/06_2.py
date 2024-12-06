import time

N = 0
E = 1
S = 2
W = 3

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def parse(src):
    grid = [['*'] + list(l) + ['*'] for l in src.splitlines()]
    grid = ['*' * len(grid[0])] + grid + ['*' * len(grid[0])]
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char in '^v<>':
                visited = [[0] * len(row) for row in grid]
                return grid, visited, x, y, {'^': N, 'v': S, '<': W, '>': E}[char]


def simulate_guard(grid, visited, x, y, d):
    for row in visited:
        for i in range(len(row)):
            row[i] = 0
    while True:
        if visited[y][x] & (1 << d):
            return None  # loop
        visited[y][x] |= (1 << d)
        nx = x + DIRS[d][0]
        ny = y + DIRS[d][1]
        if grid[ny][nx] == '*':
            return True
        if grid[ny][nx] == '#':
            d = (d + 1) & 3
        else:
            x = nx
            y = ny


def part1(src):
    grid, visited, x, y, d = parse(src)
    simulate_guard(grid, visited, x, y, d)
    return sum(sum(1 for x in row if x) for row in visited)


def part2(src):
    grid, visited, gx, gy, d = parse(src)
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != '.':
                continue
            grid[y][x] = '#'
            if not simulate_guard(grid, visited, gx, gy, d):
                count += 1
            grid[y][x] = '.'
    return count


SAMPLE = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

assert part1(SAMPLE) == 41
assert part2(SAMPLE) == 6

with open('in/06.txt', 'rt') as f:
    data = f.read()

print(part1(data))
start = time.time()
print(part2(data))
print(time.time() - start)

# cpython 43.6
# graalpy 1.2s
