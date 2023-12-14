import copy


def tilt_north(data):
    for x in range(len(data[0])):
        y = 0
        while y < len(data):
            if data[y][x] == 'O':
                while y > 0 and data[y - 1][x] == '.':
                    data[y-1][x] = 'O'
                    data[y][x] = '.'
                    y -= 1
            y += 1


def get_load(data):
    return sum((len(data) - x) for x, r in enumerate(data) for c in r if c == 'O')


def rotate(data):
    return [[c for c in reversed(x)] for x in zip(*data)]


def cycle(data):
    tilt_north(data)
    data = rotate(data)
    tilt_north(data)
    data = rotate(data)
    tilt_north(data)
    data = rotate(data)
    tilt_north(data)
    return rotate(data)


def encode(data):
    return ''.join(''.join(r) for r in data)


with open('ex/14.txt', 'rt') as f:
    d = [list(s.strip()) for s in f]


# part 1
d1 = copy.deepcopy(d)
tilt_north(d1)
print(get_load(d1))

# part 2
results = {}
i = 0
while i < 1000000000:
    encoded = encode(d)
    if encoded in results:
        start = results[encoded]
        cycle_len = i - start
        cycle_count = (1000000000 - start) // cycle_len
        i = start + (cycle_count * cycle_len)
    results[encoded] = i
    i += 1
    d = cycle(d)

print(get_load(d))
