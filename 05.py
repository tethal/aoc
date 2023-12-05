import itertools


with open('05a.txt', 'rt') as f:
    seeds = list(map(int, f.readline().split(':')[1].split()))
    maps = [tuple((tuple(map(int, x.split())) for x in b)) for a, b in itertools.groupby(f, lambda k: bool(k[0].isdigit())) if a]


def apply_map(seed):
    for m in maps:
        for r in m:
            if r[1] <= seed < r[1] + r[2]:
                seed = r[0] + seed - r[1]
                break
    return seed


print(min(apply_map(seed) for seed in seeds))
