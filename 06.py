import math


def solve(time, distance):
    d = time ** 2 - 4 * distance
    if d < 0:
        return 0
    d = math.sqrt(d)
    x1 = math.ceil((time - d) / 2 + 0.001)
    x2 = math.floor((time + d) / 2 - 0.001)
    x1 = max(0, x1)
    x2 = min(time, x2)
    return x2 - x1 + 1


with open('06a.txt', 'rt') as f:
    times = list(map(int, f.readline().split(':')[1].split()))
    distances = list(map(int, f.readline().split(':')[1].split()))

print(math.prod(solve(time, distance) for time, distance in zip(times, distances)))

t = int(''.join(str(t) for t in times))
d = int(''.join(str(d) for d in distances))
print(solve(t, d))
