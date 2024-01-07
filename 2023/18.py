
DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def parse(line):
    c = line.split(' ')
    x = int(c[2][2:-2], 16)     # remove '(#' and ')\n'
    return 'RDLU'.index(c[0]), int(c[1]), x & 15, x >> 4


def area(src):
    vertices = []
    p = (0, 0)
    border = 0
    for d, cnt, in src:
        p = (p[0] + cnt * DIRS[d][0], p[1] + cnt * DIRS[d][1])
        vertices.append(p)
        border += cnt

    vertices.insert(0, vertices[-1])
    vertices.append(vertices[1])
    a = sum(vertices[i][1] * (vertices[i - 1][0] - vertices[i + 1][0]) for i in range(1, len(vertices) - 1))
    return (border + a) // 2 + 1


with open('ex/18.txt', 'rt') as f:
    data = [parse(line) for line in f]

print(area(map(lambda x: x[:2], data)))
print(area(map(lambda x: x[2:], data)))
