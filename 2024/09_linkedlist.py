import time
from dataclasses import dataclass, field


@dataclass
class Item:
    fid: int
    length: int
    moved: bool = False
    prev: "Item" = field(default=None, repr=False)
    next: "Item" = field(default=None, repr=False)

    def is_free(self):
        return self.fid == -1


def parse(src):
    fid = 0
    block = 0
    head = None
    tail = None
    free = False
    for cc in src.strip():
        c = int(cc)
        item = Item(-1 if free else fid, c, prev=tail)
        if tail:
            tail.next = item
        else:
            head = item
        tail = item
        fid += free
        block += c
        free = not free
    return head, tail


def calc_checksum(item):
    checksum = 0
    block = 0
    while item:
        if item.is_free():
            block += item.length
        else:
            for i in range(item.length):
                checksum += block * item.fid
                block += 1
        item = item.next
    return checksum


def part1(src):
    head, tail = parse(src)
    b = head
    e = tail
    while b is not e:
        if not b.is_free() or not b.length:
            b = b.next
        elif e.is_free() or not e.length:
            e = e.prev
        else:
            copy_blocks = min(b.length, e.length)
            i = Item(e.fid, copy_blocks, prev=b.prev, next=b)
            i.prev.next = i
            i.next.prev = i
            b.length -= copy_blocks
            e.length -= copy_blocks

    return calc_checksum(head)


def part2(src):
    head, tail = parse(src)
    e = tail
    while e:
        if not e.is_free() and not e.moved:
            b = head
            while b is not e:
                if b.is_free() and b.length >= e.length:
                    i = Item(e.fid, e.length, moved=True, prev=b.prev, next=b)
                    e.fid = -1
                    i.prev.next = i
                    i.next.prev = i
                    b.length -= i.length
                    break
                b = b.next
        e = e.prev

    return calc_checksum(head)


SAMPLE = "2333133121414131402"

assert part1(SAMPLE) == 1928
assert part2(SAMPLE) == 2858

with open('in/09.txt', 'rt') as f:
    data = f.read()

print(part1(data))
start = time.time()
print(part2(data))
print(time.time() - start)
