import sys
from collections import defaultdict, deque



def run(code, inp):
    pc = 0
    ram = defaultdict(int, enumerate(code))
    modes = 0
    rel_base = 0

    def fetch():
        nonlocal pc
        v = ram[pc]
        pc += 1
        return v

    def src_val():
        nonlocal modes
        m, modes = modes % 10, modes // 10
        a = fetch()
        if m == 1:
            return a
        elif m == 2:
            return ram[rel_base + a]
        else:
            return ram[a]

    def dst_addr():
        nonlocal modes
        m, modes = modes % 10, modes // 10
        a = fetch()
        if m == 1:
            return a
        elif m == 2:
            return rel_base + a
        else:
            return a

    while True:
        op = fetch()
        modes, op = op // 100, op % 100
        if op == 1:
            a, b, c = src_val(), src_val(), dst_addr()
            ram[c] = a + b
        elif op == 2:
            a, b, c = src_val(), src_val(), dst_addr()
            ram[c] = a * b
        elif op == 3:
            a = dst_addr()
            ram[a] = next(inp)
        elif op == 4:
            a = src_val()
            yield a
        elif op == 5:
            a, b = src_val(), src_val()
            if a != 0:
                pc = b
        elif op == 6:
            a, b = src_val(), src_val()
            if a == 0:
                pc = b
        elif op == 7:
            a, b, c = src_val(), src_val(), dst_addr()
            ram[c] = 1 if a < b else 0
        elif op == 8:
            a, b, c = src_val(), src_val(), dst_addr()
            ram[c] = 1 if a == b else 0
        elif op == 9:
            a = src_val()
            rel_base += a
        elif op == 99:
            return


def create_droid(code):

    inp_queue = deque()

    def inp():
        while inp_queue:
            yield inp_queue.popleft()

    outp = run(code, inp())

    def f(movement_command):
        inp_queue.append(movement_command)
        return next(outp)

    return f


DIRS = {
    'W': (-1, 0),
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
}

DIRS_CMD = {
    'W': 3,
    'N': 1,
    'E': 4,
    'S': 2,
}

BACK_CMD = {
    'W': 4,
    'N': 2,
    'E': 3,
    'S': 1,
}


def create_maze(code):
    droid = create_droid(code)
    maze = defaultdict(lambda: ' ')

    def go(x, y, direction):
        dx, dy = DIRS[direction]
        nx, ny = x + dx, y + dy
        if maze[(nx, ny)] != ' ':
            return
        tile = droid(DIRS_CMD[direction])
        if tile == 0:
            maze[(nx, ny)] = '#'
            return
        maze[(nx, ny)] = 'X' if tile == 2 else '.'
        visit_tile(nx, ny)
        droid(BACK_CMD[direction])

    def visit_tile(x, y):
        for d in 'NESW':
            go(x, y, d)

    sys.setrecursionlimit(10000)
    maze[(0, 0)] = '.'
    visit_tile(0, 0)
    return maze


def find_x(maze):
    queue = deque([(0, 0, 0)])
    visited = set()
    while True:
        x, y, path_len = queue.popleft()
        visited.add((x, y))
        if maze[(x, y)] == 'X':
            return x, y, path_len
        path_len += 1
        for d in 'NESW':
            dx, dy = DIRS[d]
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and maze[(nx, ny)] != '#':
                queue.append((nx, ny, path_len))


def fill_maze(maze, x, y):
    queue = deque([(x, y, 0)])
    visited = set()
    max_len = 0
    while queue:
        x, y, path_len = queue.popleft()
        visited.add((x, y))
        max_len = max(max_len, path_len)
        path_len += 1
        for d in 'NESW':
            dx, dy = DIRS[d]
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and maze[(nx, ny)] != '#':
                queue.append((nx, ny, path_len))
    return max_len


with open('in/15.txt', 'rt') as f:
    code = list(map(int, f.readline().strip().split(',')))

m = create_maze(code)
xx, yy, dist = find_x(m)

print(dist)
print(fill_maze(m, xx, yy))
