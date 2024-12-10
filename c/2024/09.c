#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

#include "../util.h"


const char *SAMPLE = "2333133121414131402";

typedef struct item_t {
    int fid;
    int length;
    int moved;
    struct item_t *next;
    struct item_t *prev;
} item_t;

static void parse(const char *src, item_t **head, item_t **tail) {
    *head = NULL;
    *tail = NULL;
    int free = 0;
    int fid = 0;
    while (isdigit(*src)) {
        item_t *item = malloc(sizeof(item_t));
        item->fid = free ? -1 : fid;
        item->length = *src++ - '0';
        item->moved = 0;
        item->next = NULL;
        item->prev = *tail;
        if (*tail) {
            (*tail)->next = item;
        } else {
            *head = item;
        }
        *tail = item;
        fid += free;
        free = 1 - free;
    }
}

static void free_list(item_t *head) {
    while (head) {
        item_t *next = head->next;
        free(head);
        head = next;
    }
}

static long calc_checksum(item_t *item) {
    long checksum = 0;
    long block = 0;
    while (item) {
        if (item->fid == -1) {
            block += item->length;
        } else {
            for (int i = 0; i < item->length; ++i) {
                checksum += block * item->fid;
                block++;
            }
        }
        item = item->next;
    }
    return checksum;
}

static long part1(const char *src) {
    item_t *head, *tail;
    parse(src, &head, &tail);
    item_t *b = head;
    item_t *e = tail;
    while (b != e) {
        if (b->fid != -1 || !b->length) {
            b = b->next;
        } else if (e->fid == -1 || !e->length) {
            e = e->prev;
        } else {
            int copy_blocks = b->length < e->length ? b->length : e->length;
            item_t *i = malloc(sizeof(item_t));
            i->fid = e->fid;
            i->length = copy_blocks;
            i->prev = b->prev;
            i->next = b;
            i->prev->next = i;
            i->next->prev = i;
            b->length -= copy_blocks;
            e->length -= copy_blocks;
        }
    }
    long checksum = calc_checksum(head);
    free_list(head);
    return checksum;
}

static long part2(const char *src) {
    item_t *head, *tail;
    parse(src, &head, &tail);
    item_t *e = tail;
    while (e->prev != NULL) {
        if (e->fid != -1 && !e->moved) {
            item_t *b = head;
            while (b != e) {
                if (b->fid == -1 && b->length >= e->length) {
                    item_t *i = malloc(sizeof(item_t));
                    i->fid = e->fid;
                    i->length = e->length;
                    i->moved = 1;
                    i->prev = b->prev;
                    i->next = b;
                    i->prev->next = i;
                    i->next->prev = i;
                    e->fid = -1;
                    b->length -= i->length;
                    break;
                }
                b = b->next;
            }
        }
        e = e->prev;
    }
    long checksum = calc_checksum(head);
    free_list(head);
    return checksum;
}

int main(int argc, char *argv[]) {
    assert(part1(SAMPLE) == 1928);
    assert(part2(SAMPLE) == 2858);
    char *src = read_input("2024/in/09.txt");
    printf("%ld\n", part1(src));
    printf("%ld\n", part2(src));
    free(src);
}
