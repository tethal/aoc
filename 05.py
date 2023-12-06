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


intervals = {(s, s + l) for s, l in zip(seeds[::2], seeds[1::2])}
new_intervals = set()

for mm in maps:
    new_intervals = set()
    for m in mm:
        b_start = m[1]
        b_end = m[1] + m[2]
        delta = m[0] - m[1]

        old_intervals = intervals
        intervals = set()
        for a_start, a_end in old_intervals:
            if b_start <= a_start:
                if b_end >= a_end:
                    new_intervals.add((a_start + delta, a_end + delta))
                elif b_end > a_start:
                    new_intervals.add((a_start + delta, b_end + delta))
                    intervals.add((b_end, a_end))
                else:
                    intervals.add((a_start, a_end))
            elif b_start < a_end:
                if b_end >= a_end:
                    new_intervals.add((b_start + delta, a_end + delta))
                    intervals.add((a_start, b_start))
                else:
                    new_intervals.add((b_start + delta, b_end + delta))
                    intervals.add((a_end, b_start))
                    intervals.add((b_end, a_end))
            else:
                intervals.add((a_start, a_end))

    intervals = intervals | new_intervals

print(min(s for s, e in intervals))
