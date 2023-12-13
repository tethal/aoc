import collections
import functools

# part1:
# ranks = {k: v for v, k in enumerate(reversed("A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")))}
#
# def to_type(hand):
#     return sorted((v for k, v in collections.Counter(hand).items()), reverse=True)


# part 2:
ranks = {k: v for v, k in enumerate(reversed("A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", ")))}


def to_type(hand):
    cntr = collections.Counter(hand)
    jokers = cntr.pop('J', 0)
    if jokers == 5:
        return [5]
    r = sorted(cntr.values(), reverse=True)
    r[0] += jokers
    return r


def to_ranks(s):
    return tuple(ranks[c] for c in s)


def cmp_hands(h1, h2):
    t1, t2 = ((to_type(h), to_ranks(h)) for h in (h1[0], h2[0]))
    if t1 < t2:
        return -1
    if t1 > t2:
        return 1
    return 0


with open('ex/07.txt', 'rt') as f:
    hands = [(line.split()[0], int(line.split()[1])) for line in f]

hands = sorted(hands, key=functools.cmp_to_key(cmp_hands))

print(sum(i * h[1] for i, h in enumerate(hands, start=1)))
