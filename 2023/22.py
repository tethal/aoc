from collections import namedtuple


Coord = namedtuple('Coord', 'x y z')


class Brick:
    def __init__(self, line):
        self.start, self.end = map(lambda x: Coord(*map(int, x.split(','))), line.split('~'))
        assert self.start.z <= self.end.z
        self.supported_by = set()

    def points_of_flat_brick(self, z):
        assert self.start.z == self.end.z
        yield from ((x, y, z) for x in range(self.start.x, self.end.x + 1) for y in range(self.start.y, self.end.y + 1))

    def points_of_tall_brick(self, dz):
        assert self.start.z < self.end.z
        yield from ((self.start.x, self.start.y, z - dz) for z in range(self.start.z, self.end.z + 1))

    def would_something_fall_if_removed(self):
        return len({b2 for b2 in bricks if b2.would_fall_if_all_in_b_removed({self})}) != 0

    def would_fall_if_all_in_b_removed(self, b):
        return (b & self.supported_by) and len(self.supported_by - b) == 0

    def how_many_would_fall_if_removed(self):
        r = {self}
        old_len = 0
        while old_len < len(r):
            old_len = len(r)
            for b in bricks:
                if b.would_fall_if_all_in_b_removed(r):
                    r.add(b)
        return len(r - {self})


with open('ex/22.txt', 'rt') as f:
    bricks = list(map(Brick, f))


bricks.sort(key=lambda b: b.start.z)

data = {}

for b in bricks:
    if b.start.z == b.end.z:
        z = b.start.z
        while z > 1:
            b.supported_by = {data[p] for p in b.points_of_flat_brick(z - 1) if p in data}
            if b.supported_by:
                break
            z -= 1
        for p in b.points_of_flat_brick(z):
            data[p] = b
    else:
        z = b.start.z
        while z > 1 and (b.start.x, b.start.y, z - 1) not in data:
            z -= 1
        for p in b.points_of_tall_brick(b.start.z - z):
            data[p] = b
        if z != 1:
            b.supported_by.add(data[(b.start.x, b.start.y, z - 1)])

print(sum(1 for b in bricks if not b.would_something_fall_if_removed()))
print(sum(b.how_many_would_fall_if_removed() for b in bricks))
