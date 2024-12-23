import time
from collections import defaultdict


def parse(src):
    graph = defaultdict(set)
    for line in src.splitlines():
        a, b = line.split('-')
        graph[a].add(b)
        graph[b].add(a)
    return graph


def part1(src):
    graph = parse(src)
    result = set()
    for a, n in graph.items():
        if a[0] != 't':
            continue
        for b in n:
            for c in graph[b]:
                if a in graph[c]:
                    result.add(frozenset({a, b, c}))

    return len(result)


def part2(src):
    graph = parse(src)
    max_clique = set()
    for start_node in graph:
        clique = {start_node}
        for n in graph:
            if graph[n] & clique == clique:
                clique.add(n)
        if len(clique) > len(max_clique):
            max_clique = clique

    return ','.join(sorted(max_clique))


SAMPLE = """\
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""

assert part1(SAMPLE) == 7
assert part2(SAMPLE) == 'co,de,ka,ta'

with open('in/23.txt', 'rt') as f:
    data = f.read()

print(part1(data))
start = time.time()
print(part2(data))
print(time.time() - start)
