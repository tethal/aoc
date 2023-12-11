import itertools


with open('11a.txt', 'rt') as f:
    data = f.read().splitlines()


def calc(expansion):
    x_map = []
    x = 0
    for col in zip(*data):
        x_map.append(x)
        if all(c == '.' for c in col):
            x += expansion
        else:
            x += 1

    stars = []
    y = 0
    for row in data:
        if all(c == '.' for c in row):
            y += expansion
        else:
            for x, c in enumerate(row):
                if c == '#':
                    stars.append((x_map[x], y))
            y += 1

    return sum(abs(s1[0] - s2[0]) + abs(s1[1] - s2[1]) for s1, s2 in itertools.combinations(stars, 2))


print(calc(2))
print(calc(10))
print(calc(1000000))

