def find_digit(line, rev):
    for i in rev(range(len(line))):
        if line[i].isdigit():
            return int(line[i])
        elif v := next((x for x, name in enumerate("one,two,three,four,five,six,seven,eight,nine".split(","), start=1) if line.startswith(name, i)), None):
            return v


with open('01a.txt', 'rt') as f:
    print(sum(10 * find_digit(line, lambda x: x) + find_digit(line, reversed) for line in f))
