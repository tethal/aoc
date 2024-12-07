#include <stdio.h>
#include <stdlib.h>

#include "../util.h"


const char *SAMPLE =
"190: 10 19\n"
"3267: 81 40 27\n"
"83: 17 5\n"
"156: 15 6\n"
"7290: 6 8 6 15\n"
"161011: 16 10 13\n"
"192: 17 8 14\n"
"21037: 9 7 18 13\n"
"292: 11 6 16 20\n";

static long common(const char *src, int (*helper)(long, long, char *, char **)) {
    long sum = 0;
    while (*src) {
        char *p;
        long int total = strtol(src, &p, 10);
        p++;
        long int first = strtol(p, &p, 10);
        if (helper(total, first, p, &p)) {
            sum += total;
        }
        src = p;
    }
    return sum;
}

static int helper1(long total, long acc, char *src, char **next) {
    if (*src == '\n') {
        *next = src + 1;
        return total == acc;
    }
    char *p;
    long v = strtol(src, &p, 10);
    return helper1(total, acc + v, p, next) || helper1(total, acc * v, p, next);
}

static long long part1(const char *src) {
    return common(src, helper1);
}

static int helper2(long total, long acc, char *src, char **next) {
    if (*src == '\n') {
        *next = src + 1;
        return total == acc;
    }
    char *p;
    long v = strtol(src, &p, 10);
    if (helper2(total, acc + v, p, next) || helper2(total, acc * v, p, next)) {
        return 1;
    }
    char buf[40];
    sprintf(buf, "%ld%ld", acc, v);
    return helper2(total, strtol(buf, NULL, 10), p, next);
}

static long part2(const char *src) {
    return common(src, helper2);
}

int main(int argc, char *argv[]) {
    assert(part1(SAMPLE) == 3749);
    assert(part2(SAMPLE) == 11387);
    char *src = read_input("2024/in/07.txt");
    printf("%ld\n", part1(src));
    printf("%ld\n", part2(src));
    free(src);
}
