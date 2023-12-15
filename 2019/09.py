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


with open('in/09.txt', 'rt') as f:
    code = list(map(int, f.readline().strip().split(',')))

print(list(run(code, iter([1]))))
print(list(run(code, iter([2]))))
