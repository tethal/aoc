from util import DIRS, NE, NW, SE, SW, Vector


class Board:
    def __init__(self, src):
        self.lines = src.splitlines()
        self.w = len(self.lines[0])
        self.h = len(self.lines)

    def __iter__(self):
        return self.except_border(0)

    def except_border(self, b=1):
        for r in range(b, self.h - b):
            for c in range(b, self.w - b):
                yield Vector(c, r)

    def __getitem__(self, v):
        return self.lines[v.y][v.x] if 0 <= v.x < self.w and 0 <= v.y < self.h else None


def part1(src):
    board = Board(src)
    return sum(1
               for o in filter(lambda v: board[v] == 'X', board)
               for d in filter(lambda v: board[o + v] == 'M', DIRS)
               if board[o + d * 2] == 'A' and board[o + d * 3] == 'S'
               )


def part2(src):
    board = Board(src)
    return sum(1
               for o in filter(lambda v: board[v] == 'A', board.except_border())
               if board[o + NW] + board[o + SE] in ('MS', 'SM') and board[o + NE] + board[o + SW] in ('MS', 'SM')
               )


SAMPLE = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

assert part1(SAMPLE) == 18
assert part2(SAMPLE) == 9

with open('in/04.txt', 'rt') as f:
    data = f.read()

print(part1(data))
print(part2(data))
