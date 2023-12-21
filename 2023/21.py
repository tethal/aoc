with open('in/21.txt', 'rt') as f:
    grid = f.read().splitlines()


def find_start():
    for y, r in enumerate(grid):
        for x, c in enumerate(r):
            if c == 'S':
                return x, y


w, h = len(grid[0]), len(grid)
sx, sy = find_start()


def get_count(x, y, max_steps):
    queue = {(x, y)}
    for dist in range(max_steps):
        nq = set()
        for x, y in queue:
            for nx, ny in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
                if 0 <= nx < w and 0 <= ny < h and grid[ny][nx] in '.S':
                    nq.add((nx, ny))
        queue = nq
    return len(queue)


# part 1
print(get_count(sx, sy, 64))

# part 2
assert w == h
assert sx == sy
tiles = 26501365 // w
print(
    tiles * tiles * get_count(sx, sy, w + h) +
    (tiles - 1) * (tiles - 1) * get_count(sx, sy, w + h + 1) +
    get_count(0, sy, w - 1) +
    get_count(w - 1, sy, w - 1) +
    get_count(sx, 0, h - 1) +
    get_count(sx, h - 1, h - 1) +
    tiles * get_count(0, h - 1, sx - 1) +
    tiles * get_count(w - 1, h - 1, sx - 1) +
    tiles * get_count(w - 1, 0, sx - 1) +
    tiles * get_count(0, 0, sx - 1) +
    (tiles - 1) * get_count(0, h - 1, w + sx - 1) +
    (tiles - 1) * get_count(w - 1, h - 1, w + sx - 1) +
    (tiles - 1) * get_count(w - 1, 0, w + sx - 1) +
    (tiles - 1) * get_count(0, 0, w + sx - 1)
)


def part2_alternative():
    queue = {(sx, sy)}
    for dist in range(1000):
        if dist == sx:
            y0 = len(queue)
        if dist == sx + w:
            y1 = len(queue)
        if dist == sx + 2 * w:
            y2 = len(queue)
            c = y0
            a = (y2 - 2 * y1 + y0) // 2
            b = y1 - y0 - a
            x = (26501365 - sx) // w
            return a * x * x + b * x + c

        nq = set()
        for x, y in queue:
            for nx, ny in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
                if grid[ny % w][nx % w] in '.S':
                    nq.add((nx, ny))
        queue = nq


print(part2_alternative())
