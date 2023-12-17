import heapq
from collections import namedtuple

with open('ex/17.txt', 'rt') as f:
    costs = [list(map(int, list(line.strip()))) for line in f]

h = len(costs)
w = len(costs[0])


Item = namedtuple('Item', ['cost', 'x', 'y', 'from_x', 'from_y', 'same_dir_steps'])


def neighbours(item, min_steps, max_steps):
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx, ny = item.x + dx, item.y + dy
        if (nx, ny) == (item.from_x, item.from_y):
            continue
        steps = 0
        if (dx, dy) == (item.x - item.from_x, item.y - item.from_y):
            if item.same_dir_steps < max_steps:
                steps = item.same_dir_steps + 1
        elif item.same_dir_steps >= min_steps:
            steps = 1
        if steps and 0 <= nx < w and 0 <= ny < h:
            yield Item(item.cost + costs[ny][nx], nx, ny, item.x, item.y, steps)


def find(min_steps, max_steps):
    done = set()
    queue = []
    heapq.heappush(queue, Item(costs[1][0], 0, 1, 0, 0, 1))
    heapq.heappush(queue, Item(costs[0][1], 1, 0, 0, 0, 1))
    while queue:
        item = heapq.heappop(queue)
        if item[1:] in done:
            continue
        done.add(item[1:])
        if item.x == w - 1 and item.y == h - 1 and item.same_dir_steps >= min_steps:
            return item.cost
        for ni in neighbours(item, min_steps, max_steps):
            heapq.heappush(queue, ni)


print(find(0, 3))
print(find(4, 10))
