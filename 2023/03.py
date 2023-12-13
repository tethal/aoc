import itertools
import math


class PartNum:
    val = 0


def convert_line(line, y):
    out = []
    last = PartNum()
    for x, c in enumerate(line):
        if c.isdigit():
            last.val = 10 * last.val + int(c)
            out.append(last)
        else:
            last = PartNum()
            out.append(c)
            if c != '.':
                symbols.append((c, x, y, set()))
    return out


symbols = []
with open('ex/03.txt', 'rt') as f:
    grid = tuple(convert_line(line.strip(), y) for y, line in enumerate(f))

    for _, x, y, neighbours in symbols:
        for dx, dy in itertools.product((-1, 0, 1), repeat=2):
            if 0 <= y + dy < len(grid) and 0 <= x + dx < len(grid[y + dy]):
                cell = grid[y + dy][x + dx]
                if isinstance(cell, PartNum):
                    neighbours.add(cell)

    print(sum(part.val for part in set.union(*(s for _, _, _, s in symbols))))
    print(sum(math.prod(part.val for part in s) for c, _, _, s in symbols if c == '*' and len(s) == 2))
