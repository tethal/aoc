import copy
import math
import re
from collections import namedtuple

COND = re.compile(r'([xmas])([<>])(\d+):(\w+)')
FALLBACK = re.compile(r',(\w+)}')
PART = re.compile(r'{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}')

Rule = namedtuple('Rule', 'name conds fallback')
Cond = namedtuple('Cond', 'attr op value target')


def parse_rules(f):
    while line := f.readline().strip():
        name = line.split('{')[0]
        fallback = FALLBACK.search(line)[1]
        yield Rule(name, [Cond(a, o, int(v), t) for a, o, v, t in COND.findall(line)], fallback)


def parse_parts(f):
    while line := f.readline().strip():
        yield {k: int(v) for k, v in zip('xmas', PART.fullmatch(line).groups())}


with open('ex/19.txt', 'rt') as f:
    rules = {r.name: r for r in parse_rules(f)}
    parts = list(parse_parts(f))


# part 1
def apply(rule, part):
    for c in rule.conds:
        if c.op == '<' and part[c.attr] < c.value or c.op == '>' and part[c.attr] > c.value:
            return c.target
    return rule.fallback


def is_accepted(part):
    n = 'in'
    while n not in 'AR':
        n = apply(rules[n], part)
    return n == 'A'


print(sum(sum(p.values()) for p in parts if is_accepted(p)))


# part 2

class Interval:
    def __init__(self, start=1, end=4000):
        self.start = max(1, start)
        self.end = min(4000, end)

    def __len__(self):
        return self.end - self.start + 1 if self.end >= self.start else 0

    def split(self, cond):
        if cond.op == '>':
            return Interval(cond.value + 1, self.end), Interval(self.start, cond.value)
        else:
            return Interval(self.start, cond.value - 1), Interval(cond.value, self.end)


class Part:
    def __init__(self):
        self.x = Interval()
        self.m = Interval()
        self.a = Interval()
        self.s = Interval()

    def get_count(self):
        return math.prod(len(getattr(self, k)) for k in 'xmas')

    def split(self, cond):
        p1 = copy.copy(self)
        p2 = copy.copy(self)
        a1, a2 = getattr(self, cond.attr).split(cond)
        setattr(p1, cond.attr, a1)
        setattr(p2, cond.attr, a2)
        return p1, p2


def apply_rule(rule_name, part):
    if rule_name == 'A':
        return part.get_count()
    if rule_name == 'R':
        return 0
    r = 0
    for c in rules[rule_name].conds:
        p1, part = part.split(c)
        r += apply_rule(c.target, p1)
    return r + apply_rule(rules[rule_name].fallback, part)


print(apply_rule('in', Part()))
