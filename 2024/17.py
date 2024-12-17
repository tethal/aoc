import re
import time

RE = re.compile(r"Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n\nProgram: (\d+(,\d)*)")


def parse(src):
    *regs, program = RE.match(src).groups()[:-1]
    return *map(int, regs), list(map(int, program.split(',')))


def execute(a, b, c, program):
    def combo(o):
        return o if o < 4 else [a, b, c][o - 4]

    pc = 0
    output = []
    while pc < len(program):
        opcode = program[pc]
        operand = program[pc + 1]
        pc += 2
        match opcode:
            case 0:  # adv
                a = a >> combo(operand)
            case 1:  # bxl
                b = b ^ operand
            case 2:  # bst
                b = combo(operand) % 8
            case 3:  # jnz
                if a:
                    pc = operand
            case 4:  # bxc
                b = b ^ c
            case 5:  # out
                output.append(combo(operand) % 8)
            case 6:  # bdv
                b = a >> combo(operand)
            case 7:  # cdv
                c = a >> combo(operand)
    return output


def part1(src):
    return ','.join(map(str, execute(*parse(src))))


def part2(src):
    _, b, c, program = parse(src)

    def helper(guess, digit):
        for i in range(8):
            guess[digit] = i
            a = sum(d * 8 ** i for i, d in enumerate(guess))
            output = execute(a, b, c, program)
            if len(output) == len(program) and output[digit] == program[digit]:
                if digit == 0:
                    return a
                elif r := helper(guess, digit - 1):
                    return r

    return helper([0] * len(program), len(program) - 1)


SAMPLE = """\
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""

SAMPLE2 = """\
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""

assert part1(SAMPLE) == "4,6,3,5,6,3,5,2,1,0"
assert part2(SAMPLE2) == 117440

with open('in/17.txt', 'rt') as f:
    data = f.read()

print(part1(data))
start = time.time()
print(part2(data))
print(time.time() - start)
