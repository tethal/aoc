import sympy


def part1():
    test_range = range(7, 27 + 1)
    # test_range = range(200000000000000, 400000000000000 + 1)

    def solve(a, b, c):
        def det(x, y):
            return x[0] * y[1] - y[0] * x[1]
        d = det(a, b)
        return (det(c, b) / d, det(a, c) / d) if d else (None, None)

    def intersection(ai, vi, aj, vj):
        t, s = solve(vi, (-vj[0], -vj[1]), (aj[0] - ai[0], aj[1] - ai[1]))
        return (ai[0] + t * vi[0], ai[1] + t * vi[1]) if t is not None and t >= 0 and s >= 0 else (None, None)

    cnt = 0
    for i in range(len(data)):
        ai, vi = data[i]
        for j in range(i + 1, len(data)):
            aj, vj = data[j]
            x, y = intersection(ai, vi, aj, vj)
            if x is not None and test_range.start <= x < test_range.stop and test_range.start <= y < test_range.stop:
                cnt += 1
    return cnt


with open('ex/24.txt', 'rt') as f:
    data = tuple(tuple(map(lambda p: tuple(map(int, p.split(', '))), line.strip().split(' @ '))) for line in f)

print(part1())

# part2
sp = sympy.symbols('x y z')
sv = sympy.symbols('vx vy vz')
ts = sympy.symbols('t0 t1 t2')
eq = [sp[d] - p[d] + t * sv[d] - t * v[d] for (p, v), t in zip(data[:3], ts) for d in range(3)]
solution = sympy.solve_poly_system(eq, *sp, *sv, *ts)
print(sum(solution[0][:3]))
