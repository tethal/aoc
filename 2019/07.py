from itertools import permutations, chain


def run(ram, inp):
    pc = 0
    ram = ram[:]
    modes = 0

    def fetch():
        nonlocal pc
        v = ram[pc]
        pc += 1
        return v

    def read():
        nonlocal modes
        m, modes = modes % 10, modes // 10
        a = fetch()
        if m == 1:
            return a
        else:
            return ram[a]

    while True:
        op = fetch()
        modes, op = op // 100, op % 100
        if op == 1:
            a, b, c = read(), read(), fetch()
            ram[c] = a + b
        elif op == 2:
            a, b, c = read(), read(), fetch()
            ram[c] = a * b
        elif op == 3:
            a = fetch()
            ram[a] = next(inp)
        elif op == 4:
            a = read()
            yield a
        elif op == 5:
            a, b = read(), read()
            if a != 0:
                pc = b
        elif op == 6:
            a, b = read(), read()
            if a == 0:
                pc = b
        elif op == 7:
            a, b, c = read(), read(), fetch()
            ram[c] = 1 if a < b else 0
        elif op == 8:
            a, b, c = read(), read(), fetch()
            ram[c] = 1 if a == b else 0
        elif op == 99:
            return


def try_phase(ram, phase):
    i = 0
    for j in phase:
        i = next(run(ram, iter([j, i])))
    return i


def try_phase_part2(ram, phase):
    def amp_a():
        yield from run(ram, chain(iter([phase[0], 0]), amp_e()))

    def amp_b():
        yield from run(ram, chain(iter([phase[1]]), amp_a()))

    def amp_c():
        yield from run(ram, chain(iter([phase[2]]), amp_b()))

    def amp_d():
        yield from run(ram, chain(iter([phase[3]]), amp_c()))

    def amp_e():
        yield from run(ram, chain(iter([phase[4]]), amp_d()))

    *_, last = amp_e()
    return last


with open('in/07.txt', 'rt') as f:
    ram = list(map(int, f.readline().strip().split(',')))

print(max(try_phase(ram, phase) for phase in permutations(range(5))))
print(max(try_phase_part2(ram, phase) for phase in permutations(range(5, 10))))
