from collections import defaultdict
from itertools import islice
from typing import Dict, Tuple


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


def batched(iterable, n):
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


DIRS = ((0, -1), (1, 0), (0, 1), (-1, 0))


def robot(code, start_color):
    board: Dict[Tuple[int, int], int] = defaultdict(int)
    pos = (0, 0)
    direction = 0
    if start_color:
        board[pos] = 1

    def read_board():
        while True:
            yield board[pos]

    for c, d in batched(run(code, read_board()), 2):
        board[pos] = c
        if d == 1:
            direction = (direction + 1) % 4
        else:
            direction = (direction + 3) % 4
        pos = (pos[0] + DIRS[direction][0], pos[1] + DIRS[direction][1])
    return board


def draw(board):
    min_x = min(x for x, y in board)
    min_y = min(y for x, y in board)
    max_x = max(x for x, y in board)
    max_y = max(y for x, y in board)
    for y in range(min_y, max_y + 1):
        print(''.join('#' if board[(x, y)] == 1 else '.' for x in range(min_x, max_x + 1)))


with open('in/11.txt', 'rt') as f:
    code = list(map(int, f.readline().strip().split(',')))

print(len(robot(code, 0)))
draw(robot(code, 1))
