import time
from functools import cache


class Keypad:
    def __init__(self, buttons):
        self.keys = {button: (i % 3, i // 3) for i, button in enumerate(buttons)}

    @cache
    def __getitem__(self, item):
        sx, sy = self.keys[item[0]]
        ex, ey = self.keys[item[1]]
        empty_x, empty_y = self.keys[' ']

        def helper(path, x, y):
            if x == empty_x and y == empty_y:
                return
            if x == ex and y == ey:
                yield path
            if x < ex:
                yield from helper(path + '>', x + 1, y)
            if x > ex:
                yield from helper(path + '<', x - 1, y)
            if y < ey:
                yield from helper(path + 'v', x, y + 1)
            if y > ey:
                yield from helper(path + '^', x, y - 1)

        return tuple(helper('', sx, sy))


NUMPAD = Keypad("789456123 0A")
DIRPAD = Keypad(" ^A<v>")


@cache
def solve(code, robots, keypad=DIRPAD):
    if robots == 0:
        return len(code)

    return sum(min(solve(path + 'A', robots - 1) for path in keypad[a, b]) for a, b in zip('A' + code, code))


def common(src, robots):
    return sum(solve(code, robots + 1, NUMPAD) * int(code[:-1]) for code in src.splitlines())


def part1(src):
    return common(src, 2)


def part2(src):
    return common(src, 25)


SAMPLE = """\
029A
980A
179A
456A
379A
"""

assert part1(SAMPLE) == 126384

with open('in/21.txt', 'rt') as f:
    data = f.read()

print(part1(data))
start = time.time()
print(part2(data))
print(time.time() - start)
