import time
from dataclasses import dataclass


@dataclass
class Item:
    fid: int
    length: int
    has_moved: bool = False

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
    by_length = [list(item for item in disk if not item.is_free() and item.length <= i) for i in range(10)]

    def find_last_fitting(max_len):
        while by_length[max_len]:
            item = by_length[max_len].pop()
            if not item.has_moved:
                return item

    b = 0
    block = 0
    checksum = 0
    while b < len(disk):
        if not disk[b].is_free():
            item = disk[b]
            b += 1
        else:
            if (item := find_last_fitting(disk[b].length)) is None:
                block += disk[b].length
                b += 1
                continue
            disk[b].length -= item.length
        for _ in range(item.length):
            checksum += block * item.fid
            block += 1
        item.fid = -1
        item.has_moved = True
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
