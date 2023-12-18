from collections import defaultdict


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


with open('in/17.txt', 'rt') as f:
    code = list(map(int, f.readline().strip().split(',')))

maze = ''.join(map(chr, run(code, iter([])))).splitlines()[:-1]
w = len(maze[0])
h = len(maze)


def intersections():
    for y in range(1, len(maze) - 1):
        for x in range(1, len(maze[0]) - 1):
            if maze[y][x] == '#' and maze[y - 1][x] == '#' and maze[y + 1][x] == '#' and maze[y][x - 1] == '#' and maze[y][x + 1] == '#':
                yield x, y


print(sum(x * y for x, y in intersections()))

for y, r in enumerate(maze):
    for x, c in enumerate(r):
        if c in '^<>v':
            p = (x, y)
            d = c


DIRS = {'^': (0, -1), '<': (-1, 0), '>': (1, 0), 'v': (0, 1), 'o': (0, 0)}
TURN_L = {'^': '<', '<': 'v', 'v': '>', '>': '^'}
TURN_R = {'^': '>', '>': 'v', 'v': '<', '<': '^'}


def get(p, d):
    x, y = p[0] + DIRS[d][0], p[1] + DIRS[d][1]
    return maze[y][x] if 0 <= x < w and 0 <= y < h else '.'


ins = []
while True:
    if get(p, TURN_R[d]) == '#':
        t = 'R'
        d = TURN_R[d]
    elif get(p, TURN_L[d]) == '#':
        t = 'L'
        d = TURN_L[d]
    else:
        break

    cnt = 0
    while get(p, d) == '#':
        cnt += 1
        p = (p[0] + DIRS[d][0], p[1] + DIRS[d][1])

    ins.append(f'{t},{cnt}')


def rec(functions, inp, sol):
    if len(sol) - 1 > 20:
        return None
    for f in functions:
        if len(','.join(f)) > 20:
            return None
    if not inp:
        return functions, sol
    for i, f in enumerate(functions):
        if inp[:len(f)] == f:
            if s := rec(functions, inp[len(f):], sol + chr(65 + i) + ','):
                return s
    if len(functions) == 3:
        return None
    for i in range(1, len(inp)):
         if s := rec(functions + [inp[:i]], inp[i:], sol + chr(65 + len(functions)) + ','):
             return s


fun, sol = rec([], ins, '')

code[0] = 2
src = sol[:-1] + '\n'
for f in fun:
    src += ','.join(f) + '\n'
src += 'n\n'

for x in run(code, map(ord, src)):
    if x > 255:
        print(x)
