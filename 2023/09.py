import itertools


def predict(src):
    first = []
    last = []
    while any(bool(i) for i in src):
        first.append(src[0])
        last.append(src[-1])
        src = [b - a for a, b in zip(src, src[1:])]
    return sum(last), sum(a * b for a, b in zip(first, itertools.cycle((1, -1))))


with open('ex/09.txt', 'rt') as f:
    print(tuple(map(sum, zip(*(predict(tuple(map(int, line.split()))) for line in f)))))
