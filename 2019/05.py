def run(ram, inp):
    pc = 0
    ram = ram[:]
    outp = []
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
            ram[a], inp = inp[0], inp[1:]
        elif op == 4:
            a = read()
            outp.append(a)
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
            return outp


with open('in/05.txt', 'rt') as f:
    ram = list(map(int, f.readline().strip().split(',')))

print(run(ram, [1]))
print(run(ram, [5]))
