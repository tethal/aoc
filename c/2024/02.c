#include <stdio.h>
#include <stdlib.h>

#include "../util.h"


const char *SAMPLE =
"7 6 4 2 1\n"
"1 2 7 8 9\n"
"9 7 6 2 1\n"
"1 3 2 4 5\n"
"8 6 4 4 1\n"
"1 3 6 7 9\n";

static const char *parse_report(const char *src, long_array_list_t *report) {
    long_array_list_clear(report);
    while (*src != '\n' && *src != '\r' && *src != '\0') {
        char *p;
        long_array_list_append(report, strtol(src, &p, 10));
        src = p;
    }
    while (*src == '\n' || *src == '\r') {
        src++;
    }
    return src;
}

static int sign(long v) {
    return v < 0 ? -1 : v > 0 ? 1 : 0;
}

static int is_safe(const long_array_list_t *report) {
    long_array_list_t deltas;
    long_array_list_init(&deltas);

    for (int i = 1; i < long_array_list_size(report); i++) {
        long_array_list_append(&deltas, long_array_list_get(report, i) - long_array_list_get(report, i - 1));
    }

    int first_sign = sign(long_array_list_get(&deltas, 0));
    int safe = 1;
    for (int i = 0; i < long_array_list_size(&deltas); i++) {
        long delta = long_array_list_get(&deltas, i);
        long delta_sign = sign(delta);
        long abs_delta = delta * delta_sign;
        if (abs_delta < 1 || abs_delta > 3 || delta_sign != first_sign) {
            safe = 0;
            break;
        }
    }

    long_array_list_free(&deltas);
    return safe;
}

typedef int (is_safe_callback_t)(const long_array_list_t *report);

static long common(const char *src, is_safe_callback_t is_safe_callback) {
    long_array_list_t report;
    long_array_list_init(&report);

    int safe_count = 0;
    while (*src) {
        src = parse_report(src, &report);
        if (is_safe_callback(&report)) {
            safe_count++;
        }
    }
    long_array_list_free(&report);
    return safe_count;
}

static long part1(const char *src) {
    return common(src, is_safe);
}

static int is_dumped_safe(const long_array_list_t *report) {
    long_array_list_t dumped;
    long_array_list_init(&dumped);

    int result = 0;
    for (size_t skip = 0; skip < long_array_list_size(report); skip++) {
        long_array_list_clear(&dumped);
        for (size_t i = 0; i < long_array_list_size(report); i++) {
            if (i != skip) {
                long_array_list_append(&dumped, long_array_list_get(report, i));
            }
        }
        if (is_safe(&dumped)) {
            result = 1;
            break;
        }
    }
    long_array_list_free(&dumped);
    return result;
}

static long part2(const char *src) {
    return common(src, is_dumped_safe);
}

int main(int argc, char *argv[]) {
    assert(part1(SAMPLE) == 2);
    assert(part2(SAMPLE) == 4);
    char *src = read_input("2024/in/02.txt");
    printf("%ld\n", part1(src));
    printf("%ld\n", part2(src));
    free(src);
}
