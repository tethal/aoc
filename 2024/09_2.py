import time
from dataclasses import dataclass, field


@dataclass
class Item:
    fid: int
    length: int
    children: list["Item"] = field(default_factory=list)

    def is_free(self):
        return self.fid == -1


def parse(src):
    fid = 0
    block = 0
    disk = []
    free = False
    for cc in src.strip():
        c = int(cc)
        disk.append(Item(-1 if free else fid, c))
        fid += free
        block += c
        free = not free
    return disk, sum(item.length for item in disk if not item.is_free())


def part1(src):
    disk, used = parse(src)
    checksum = 0
    b = 0
    e = -1
    for block in range(used):
        while not disk[b].length:
            b += 1
        if not disk[b].is_free():
            assert disk[b].length
            fid = disk[b].fid
        else:
            while disk[e].is_free() or not disk[e].length:
                e -= 1
            fid = disk[e].fid
            disk[e].length -= 1
        disk[b].length -= 1
        checksum += block * fid
    return checksum


def part2(src):
    disk, used = parse(src)
    e = len(disk) - 1
    while e >= 0:
        item = disk[e]
        if item.is_free():
            e -= 1
            continue
        for b in range(0, e):
            i2 = disk[b]
            if i2.is_free() and i2.length >= item.length:
                i2.children.append(item)
                i2.length -= item.length
                disk[e] = Item(-1, item.length)
                break
        e -= 1

    checksum = 0
    block = 0
    for item in disk:
        for i2 in item.children:
            for i in range(i2.length):
                checksum += block * i2.fid
                block += 1
        if item.is_free():
            block += item.length
        else:
            for i in range(item.length):
                checksum += block * item.fid
                block += 1
    return checksum


SAMPLE = "2333133121414131402"

assert part1(SAMPLE) == 1928
assert part2(SAMPLE) == 2858

with open('in/09.txt', 'rt') as f:
    data = f.read()

print(part1(data))
start = time.time()
print(part2(data))
print(time.time() - start)
