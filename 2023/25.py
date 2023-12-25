import random

nodes = set()
edges = []
with open('in/25.txt', 'rt') as f:
    for line in f:
        l, r = line.strip().split(':')
        nodes.add(l)
        nodes.update(r.split())
        edges.extend((l, x) for x in r.split())


def karger(nodes, edges):
    while len(nodes) > 2:
        u, v = random.choice(edges)
        uv = u + v
        new_edges = []
        for a, b in edges:
            if a == u and b != v or a == v and b != u:
                new_edges.append((uv, b))
            if b == u and a != v or b == v and a != u:
                new_edges.append((uv, a))
            if a != u and a != v and b != u and b != v:
                new_edges.append((a, b))
            edges = new_edges
        nodes.remove(u)
        nodes.remove(v)
        nodes.add(uv)
    return nodes, edges


while True:
    (n1, n2), e = karger(nodes.copy(), edges)
    if len(e) == 3:
        print(len(n1) * len(n2) / 9)
        break
