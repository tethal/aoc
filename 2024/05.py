from collections import defaultdict


def parse(src):
    rules, updates = src.strip().split("\n\n")
    edges = defaultdict(set)
    for line in rules.split("\n"):
        a, b = map(int, line.split("|"))
        edges[a].add(b)
    updates = [tuple(map(int, line.split(","))) for line in updates.split("\n")]
    return edges, updates


def check_rules(update, rules):
    return all(not any(b in update[:i] for b in rules[page]) for i, page in enumerate(update))


def middle(pages):
    return pages[len(pages) // 2]


def part1(src):
    rules, updates = parse(src)
    return sum(middle(update) for update in updates if check_rules(update, rules))


def topo_sort(update, rules):
    result = []
    todo = set(update)
    visited = set()

    def visit(n):
        if n not in todo:
            return
        assert n not in visited
        visited.add(n)
        for b in rules[n]:
            visit(b)
        todo.remove(n)
        result.append(n)

    while todo:
        visit(next(iter(todo)))

    return result


def part2(src):
    rules, updates = parse(src)
    return sum(middle(topo_sort(update, rules)) for update in updates if not check_rules(update, rules))


SAMPLE = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

assert part1(SAMPLE) == 143
assert part2(SAMPLE) == 123

with open('in/05.txt', 'rt') as f:
    data = f.read()

print(part1(data))
print(part2(data))
