def part1(src):
    pos = 0+0j          # starting position (origin)
    dir = 0+1j          # starting direction (north)

    for instruction in src.split(', '):
        dir *= 1j if instruction[0] == 'L' else -1j
        pos += int(instruction[1:]) * dir

    return int(abs(pos.real) + abs(pos.imag))

def part2(src):
    pos = 0+0j          # starting position (origin)
    dir = 0+1j          # starting direction (north)
    visited = {pos}

    for instruction in src.split(', '):
        dir *= 1j if instruction[0] == 'L' else -1j
        for i in range(int(instruction[1:])):
            pos += dir
            if pos in visited:
                return int(abs(pos.real) + abs(pos.imag))
            visited.add(pos)


assert part1("R2, R2, R1, L1") == 4
assert part1("R2, L3") == 5
assert part1("R2, R2, R2") == 2
assert part1("R5, L5, R5, R3") == 12
assert part2("R1, R1, R1, R2") == 0

with open('in/01.txt', 'rt') as f:
    data = f.read()

print(part1(data))
print(part2(data))
