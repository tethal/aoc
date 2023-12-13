from itertools import groupby


def is_mirror(p, i, cnt):
    for j in range(cnt):
        if p[i + j] != p[-(j+1)]:
            return False
    return True


def find_mirror(p, t):
    for i in range(len(p) - 1):
        if p[i] == p[-1] and (len(p) - i) % 2 == 0:
            cnt = (len(p) - i) // 2
            mirror = i + cnt
            if is_mirror(p, i, cnt):
                return t(mirror)
    return 0


def find(p, ignore=-1):
    if m := find_mirror(p, lambda x: 100 * x):
        if m != ignore:
            return m
    if m := find_mirror(list(reversed(p)), lambda x: 100 * (len(p) - x)):
        if m != ignore:
            return m

    p = list(zip(*p))
    if m := find_mirror(p, lambda x: x):
        if m != ignore:
            return m
    if m := find_mirror(list(reversed(p)), lambda x: len(p) - x):
        if m != ignore:
            return m


def find_part2(pattern):
    old = find(pattern)
    for y in range(len(pattern)):
        for x in range(len(pattern[0])):
            pattern[y][x] = '#' if pattern[y][x] == '.' else '.'
            if new := find(pattern, old):
                return new
            pattern[y][x] = '#' if pattern[y][x] == '.' else '.'


with open('13a.txt', 'rt') as f:
    patterns = list([list(l) for l in v] for k, v in groupby(f.read().splitlines(), key=lambda x: bool(x)) if k)


print(sum(find(pattern) for pattern in patterns))
print(sum(find_part2(pattern) for pattern in patterns))
