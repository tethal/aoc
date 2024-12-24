import operator
import re
import time
from itertools import combinations
from random import randrange

RE = re.compile(r'(\w+) (\w+) (\w+) -> (\w+)')

OP = {'AND': operator.and_, 'OR': operator.or_, 'XOR': operator.xor}


def parse(src):
    a, b = src.split('\n\n')
    wires = {l.split(':')[0]: int(l[-1]) for l in a.splitlines()}
    gates = {c: (g, a, b) for a, g, b, c in RE.findall(b)}
    return wires, gates


def evaluate(gates, wires, bits=100):
    def eval_wire(name):
        if name not in wires:
            g, a, b = gates[name]
            wires[name] = OP[g](eval_wire(a), eval_wire(b))
        return wires[name]

    result = 0
    for i in range(bits):
        name = f"z{i:0>2}"
        if name not in gates:
            return result
        result |= eval_wire(name) << i
    return result


def check_sum(gates, x, y, bits):
    wires = {}
    for i in range(45):
        wires[f'x{i:0>2}'] = 1 if x & (1 << i) else 0
        wires[f'y{i:0>2}'] = 1 if y & (1 << i) else 0
    mask = (1 << bits) - 1
    try:
        return (x + y) & mask == evaluate(gates, wires, bits) & mask
    except RecursionError:
        return False


def part1(src):
    wires, gates = parse(src)
    return evaluate(gates, wires)


def part2(src):
    wires, gates = parse(src)

    def verify_bits(bits):
        return all(check_sum(gates, randrange(1 << bits), randrange(1 << bits), bits) for _ in range(3 * bits))

    def remove_gates(fg, name):
        if name in fg:
            fg.remove(name)
        if name in gates:
            _, a, b = gates[name]
            remove_gates(fg, a)
            remove_gates(fg, b)
        return fg

    def fix_bits(bits, swaps):
        if len(swaps) > 8:
            return None
        if bits > 45:
            return swaps
        if verify_bits(bits):
            return fix_bits(bits + 1, swaps)
        for a, b in combinations(remove_gates(gates.keys() - swaps, f'z{bits - 2:0>2}'), 2):
            gates[a], gates[b] = gates[b], gates[a]
            if verify_bits(bits):
                if s := fix_bits(bits + 1, swaps | {a, b}):
                    return s
            gates[a], gates[b] = gates[b], gates[a]

    return ','.join(sorted(fix_bits(1, set())))


SAMPLE = """\
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
"""

assert part1(SAMPLE) == 2024

with open('in/24.txt', 'rt') as f:
    data = f.read()

print(part1(data))
start = time.time()
print(part2(data))
print(time.time() - start)
