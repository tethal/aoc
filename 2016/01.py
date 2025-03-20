def part1(src):
    x, y = 0, 0         # starting position (origin)
    dx, dy = 0, 1       # starting direction (north)

    for instruction in src.split(', '):
        if instruction[0] == 'L':
            dx, dy = -dy, dx
        else: # instruction must be Rd
            dx, dy = dy, -dx
        d = int(instruction[1:])
        x, y = x + d * dx, y + d * dy

    return abs(x) + abs(y)

def part2(src):
    x, y = 0, 0         # starting position (origin)
    dx, dy = 0, 1       # starting direction (north)
    visited = {(x, y)}

    for instruction in src.split(', '):
        if instruction[0] == 'L':
            dx, dy = -dy, dx
        else: # instruction must be Rd
            dx, dy = dy, -dx
        for i in range(int(instruction[1:])):
            x, y = x + dx, y + dy
            if (x, y) in visited:
                return abs(x) + abs(y)
            visited.add((x, y))

assert part2("R8, R4, R4, R8") == 4


assert part1("R2, R2, R1, L1") == 4
assert part1("R2, L3") == 5
assert part1("R2, R2, R2") == 2
assert part1("R5, L5, R5, R3") == 12
assert part2("R8, R4, R4, R8") == 4
assert part2("R1, R1, R1, R2") == 0

with open('in/01.txt', 'rt') as f:
    data = f.read()

print(part1(data))
print(part2(data))
