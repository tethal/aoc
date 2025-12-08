import math
from itertools import islice, combinations


def dist(a, b):
    return sum((a1 - b1)**2 for a1, b1 in zip(a, b))

def parse(src):
    data = [tuple(map(int, l.split(','))) for l in src.splitlines()]
    circuits = {coords: frozenset({coords}) for coords in data}
    pairs = sorted(combinations(data, 2), key=lambda pair: dist(*pair))
    return circuits, pairs

def part1(src, count=1000):
    circuits, pairs = parse(src)
    for a, b in islice(pairs, count):
        circuit = circuits[a] | circuits[b]
        for c in circuit:
            circuits[c] = circuit
    return math.prod(map(len, islice(sorted(set(circuits.values()), key=len, reverse=True), 3)))

def part2(src):
    circuits, pairs = parse(src)
    for a, b in pairs:
        circuit = circuits[a] | circuits[b]
        if len(circuit) == len(circuits):
            return a[0] * b[0]
        for c in circuit:
            circuits[c] = circuit


SAMPLE = """\
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

assert part1(SAMPLE, 10) == 40
assert part2(SAMPLE) == 25272

with open('in/08.txt', 'rt') as f:
    data = f.read()

print(part1(data))
print(part2(data))
