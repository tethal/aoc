
def memoize(fun):
    cache = {}

    def wrapper(d, runs):
        k = (d, runs)
        r = cache.get(k, None)
        if r is None:
            r = fun(d, runs)
            cache[k] = r
        return r
    return wrapper


@memoize
def solve(d, runs):
    if not d:
        return 0 if runs else 1
    if d[0] in '.':
        return solve(d[1:], runs)
    if d[0] == '#':
        if not runs or len(d) < runs[0] or '.' in d[:runs[0]]:
            return 0
        d = d[runs[0]:]
        if d and d[0] == '#':
            return 0
        return solve(d[1:], runs[1:])
    assert d[0] == '?'
    return solve(d[1:], runs) + solve('#' + d[1:], runs)


with open('ex/12.txt', 'rt') as f:
    rows = [(s.split()[0], tuple(map(int, s.split()[1].strip().split(',')))) for s in f]

print(sum(solve(*row) for row in rows))

rows = [
    ('?'.join([r[0]]*5), r[1] * 5)
    for r in rows
]

print(sum(solve(*row) for row in rows))
