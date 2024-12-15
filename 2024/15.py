import time

from util import DIR_FROM_CHAR, E, Vector, W


def part1(src):
    a, moves = src.split("\n\n")
    moves = moves.replace("\n", "")
    grid = {}
    for y, row in enumerate(a.split("\n")):
        for x, char in enumerate(row):
            if char == '@':
                pos = Vector(x, y)
                char = '.'
            grid[Vector(x, y)] = char
    for d in map(DIR_FROM_CHAR.get, moves):
        new_pos = pos + d
        if grid[new_pos] == 'O':
            p2 = new_pos
            while grid[p2] == 'O':
                p2 += d
            if grid[p2] == '.':
                grid[p2] = 'O'
                grid[new_pos] = '.'
        if grid[new_pos] == '.':
            pos = new_pos

    result = 0
    for v, char in grid.items():
        if char == 'O':
            result += 100 * v.y + v.x

    return result


def part2(src):
    a, moves = src.split("\n\n")
    moves = moves.replace("\n", "")
    grid = {}
    h = len(a.split("\n"))
    w = 2 * len(a.split("\n")[0])
    for y, row in enumerate(a.split("\n")):
        for x, char in enumerate(row):
            if char == '@':
                pos = Vector(2 * x, y)
                char = '.'
            obj = {'.': '..', 'O': '[]', '#': '##'}[char]
            grid[Vector(2 * x + 0, y)] = obj[0]
            grid[Vector(2 * x + 1, y)] = obj[1]

    def move_stone_horizontal(v, d):
        nv = v
        while grid[nv] in '[]':
            nv += d
        while grid[nv] == '.' and nv != v:
            pv = nv - d
            grid[nv] = grid[pv]
            grid[pv] = '.'
            nv = pv

    def can_part_move(v, d):
        return grid[v + d] == '.' or (grid[v + d] in '[]' and can_stone_move(v + d, d))

    def can_stone_move(v, d):
        other_part_dir = E if grid[v] == '[' else W
        return can_part_move(v, d) and can_part_move(v + other_part_dir, d)

    def move_stone_vertical(v, d):
        if can_stone_move(v, d):
            other_part_dir = E if grid[v] == '[' else W
            move_part_vertical(v, d)
            move_part_vertical(v + other_part_dir, d)

    def move_part_vertical(v, d):
        if grid[v + d] in '[]':
            move_stone_vertical(v + d, d)
        if grid[v + d] == '.':
            grid[v + d] = grid[v]
            grid[v] = '.'

    for d in map(DIR_FROM_CHAR.get, moves):
        new_pos = pos + d
        if grid[new_pos] in '[]':
            if d in (W, E):
                move_stone_horizontal(new_pos, d)
            else:
                move_stone_vertical(new_pos, d)
        if grid[new_pos] == '.':
            pos = new_pos

    result = 0
    for v, char in grid.items():
        if char == '[':
            result += 100 * v.y + v.x

    return result


SAMPLE = """\
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
"""

SAMPLE2 = """\
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""

SAMPLE3 = """\
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
"""

assert part1(SAMPLE) == 2028
assert part1(SAMPLE2) == 10092
# part2(SAMPLE3)
assert part2(SAMPLE2) == 9021

with open('in/15.txt', 'rt') as f:
    data = f.read()

print(part1(data))
start = time.time()
print(part2(data))
print(time.time() - start)
