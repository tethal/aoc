from functools import reduce


def hsh(s):
    return reduce(lambda r, c: ((r + ord(c)) * 17) & 255, s, 0)


with open('ex/15.txt', 'rt') as f:
    inp = f.readline().strip().split(',')

# part 1
print(sum(hsh(s) for s in inp))

# part 2
boxes = [[] for _ in range(256)]
for s in inp:
    if '-' in s:
        h = hsh(s[:-1])
        boxes[h] = [i for i in boxes[h] if i[0] != s[:-1]]
    if '=' in s:
        k, v = s.split('=')
        h = hsh(k)
        for i in boxes[h]:
            if i[0] == k:
                i[1] = int(v)
                break
        else:
            boxes[h].append([k, int(v)])

print(sum(b * s * y[1] for b, x in enumerate(boxes, start=1) for s, y in enumerate(x, start=1)))
