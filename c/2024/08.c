#include <stdio.h>
#include <stdlib.h>

#include "../util.h"


const char *SAMPLE =
"............\n"
"........0...\n"
".....0......\n"
".......0....\n"
"....0.......\n"
"......A.....\n"
"............\n"
"............\n"
"........A...\n"
".........A..\n"
"............\n"
"............\n";

typedef struct {
    int x, y;
} vector_t;

static void process_vector(const vector_t *a, const vector_t *b, int scalar, array_list_t *results, int w, int h) {
    vector_t c = {a->x + scalar * (b->x - a->x), a->y + scalar * (b->y - a->y)};
    if (c.x >= 0 && c.x < w && c.y >= 0 && c.y < h) {
        for (size_t i = 0; i < array_list_size(results); ++i) {
            vector_t *v = array_list_get(results, i);
            if (v->x == c.x && v->y == c.y) {
                return;
            }
        }
        array_list_append(results, &c);
    }
}

static long long common(const char *src, int part) {
    array_list_t antennas['z' - '0' + 1];
    for (int i = '0'; i <= 'z'; ++i) {
        array_list_init(&antennas[i - '0'], sizeof(vector_t));
    }
    int x = 0;
    int w = 0;
    int h = 0;
    while (*src) {
        char c = *src++;
        if (c == '\n') {
            h++;
            w = x;
            x = 0;
            continue;
        }
        if (c == '.') {
            x++;
            continue;
        }
        vector_t *v = array_list_append(&antennas[c - '0'], NULL);
        v->x = x;
        v->y = h;
        x++;
    }

    array_list_t results;
    array_list_init(&results, sizeof(vector_t));

    for (int i = '0'; i <= 'z'; ++i) {
        array_list_t *list = &antennas[i - '0'];
        for (size_t a_i = 0; a_i < array_list_size(list); ++a_i) {
            vector_t *a = array_list_get(list, a_i);
            for (size_t b_i = 0; b_i < array_list_size(list); ++b_i) {
                if (a_i == b_i) {
                    continue;
                }
                vector_t *b = array_list_get(list, b_i);
                if (part == 1) {
                    process_vector(a, b, 2, &results, w, h);
                } else {
                    for (int scalar = 0; scalar <= 60; ++scalar) {
                        process_vector(a, b, scalar, &results, w, h);
                    }
                }
            }
        }
    }
    size_t count = array_list_size(&results);
    array_list_free(&results, NULL);
    for (int i = '0'; i <= 'z'; ++i) {
        array_list_free(&antennas[i - '0'], NULL);
    }
    return count;
}

static long part1(const char *src) {
    return common(src, 1);
}

static long part2(const char *src) {
    return common(src, 2);
}

int main(int argc, char *argv[]) {
    assert(part1(SAMPLE) == 14);
    assert(part2(SAMPLE) == 34);
    char *src = read_input("2024/in/08.txt");
    printf("%ld\n", part1(src));
    printf("%ld\n", part2(src));
    free(src);
}
