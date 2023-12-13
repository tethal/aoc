def run(ram, noun, verb):
    pc = 0
    ram = ram[:]
    ram[1] = noun
    ram[2] = verb

    def fetch():
        nonlocal pc
        v = ram[pc]
        pc += 1
        return v

    while True:
        op = fetch()
        if op == 1:
            a, b, c = fetch(), fetch(), fetch()
            ram[c] = ram[a] + ram[b]
        if op == 2:
            a, b, c = fetch(), fetch(), fetch()
            ram[c] = ram[a] * ram[b]
        if op == 99:
            return ram[0]


with open('in/02.txt', 'rt') as f:
    ram = list(map(int, f.readline().strip().split(',')))

print(run(ram, 12, 2))

for noun in range(100):
    for verb in range(100):
        if run(ram, noun, verb) == 19690720:
            print(100 * noun + verb)

