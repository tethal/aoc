import math
from collections import deque

types = {}
dest = {}

with open('in/20.txt', 'rt') as f:
    for line in f:
        name, r = line.strip().split(' -> ')
        if not name[0].isalpha():
            tt, name = name[0], name[1:]
            types[name] = tt
        dest[name] = r.split(', ')

def handle_signal(state, queue, sender, mod, signal):
    if mod not in types:
        if mod in dest:
            queue.extend((mod, d, signal) for d in dest[mod])
    elif types[mod] == '%' and not signal:
        state[mod] = not state[mod]
        queue.extend((mod, d, state[mod]) for d in dest[mod])
    elif types[mod] == '&':
        state[mod][sender] = signal
        s = not all(state[mod].values())
        queue.extend((mod, d, s) for d in dest[mod])


def part1():
    cnt = {True: 0, False: 0}
    state = {k: False if t == '%' else {x: False for x, d in dest.items() if k in d} for k, t in types.items()}
    for i in range(1000):
        queue = deque([('button', 'broadcaster', False)])
        while queue:
            sender, mod, signal = queue.popleft()
            cnt[signal] += 1
            handle_signal(state, queue, sender, mod, signal)
    print(cnt[True] * cnt[False])


def part2():
    rx_inputs = [n for n, d in dest.items() if 'rx' in d]
    assert len(rx_inputs) == 1, 'unsupported number of inputs to rx'
    rx_input = rx_inputs[0]
    assert types[rx_input] == '&', 'unsupported module type of the input to rx'

    def measure_cycle(start):
        state = {k: False if t == '%' else {x: False for x, d in dest.items() if k in d} for k, t in types.items()}
        cnt = 0
        while True:
            queue = deque([('broadcaster', start, False)])
            cnt += 1
            while queue:
                sender, mod, signal = queue.popleft()
                if mod == rx_input and signal:
                    return cnt
                handle_signal(state, queue, sender, mod, signal)

    print(math.lcm(*(measure_cycle(x) for x in dest['broadcaster'])))


part1()
part2()
