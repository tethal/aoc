
def predict(src):
    if not any(bool(i) for i in src):
        return 0, 0
    p = predict([b - a for a, b in zip(src, src[1:])])
    return src[0] - p[0], src[-1] + p[1]


with open('09a.txt', 'rt') as f:
    print(tuple(map(sum, zip(*(predict(tuple(map(int, line.split()))) for line in f)))))
