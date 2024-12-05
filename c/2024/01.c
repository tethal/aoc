#include <stdio.h>
#include <stdlib.h>

#include "../util.h"


const char *SAMPLE =
"3   4\n"
"4   3\n"
"2   5\n"
"1   3\n"
"3   9\n"
"3   3\n";

static void parse(const char *src, long_array_list_t *left, long_array_list_t *right) {
    while (*src) {
        char *p;
        long_array_list_append(left, strtol(src, &p, 10));
        long_array_list_append(right, strtol(p, &p, 10));
        while (*p == '\n' || *p == '\r') {
            p++;
        }
        src = p;
    }
}

static long part1(const char *src) {
    long_array_list_t left, right;
    long_array_list_init(&left);
    long_array_list_init(&right);

    parse(src, &left, &right);
    long_array_list_sort(&left);
    long_array_list_sort(&right);

    long result = 0;
    for (int i = 0; i < long_array_list_size(&left); i++) {
        result += abs(long_array_list_get(&left, i) - long_array_list_get(&right, i));
    }

    long_array_list_free(&left);
    long_array_list_free(&right);
    return result;
}

static long part2(const char *src) {
    long_array_list_t left, right;
    long_array_list_init(&left);
    long_array_list_init(&right);

    parse(src, &left, &right);

    long result = 0;
    for (int i = 0; i < long_array_list_size(&left); i++) {
        for (int j = 0; j < long_array_list_size(&right); j++) {
            long l = long_array_list_get(&left, i);
            long r = long_array_list_get(&right, j);
            if (l == r) {
                result += l;
            }
        }
    }

    long_array_list_free(&left);
    long_array_list_free(&right);
    return result;
}

int main(int argc, char *argv[]) {
    assert(part1(SAMPLE) == 11);
    assert(part2(SAMPLE) == 31);
    char *src = read_input("2024/in/01.txt");
    printf("%ld\n", part1(src));
    printf("%ld\n", part2(src));
    free(src);
}
