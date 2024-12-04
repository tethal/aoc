#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../util.h"


const char *SAMPLE =
"MMMSXXMASM\n"
"MSAMXMSMSA\n"
"AMXSXMAAMM\n"
"MSAMASMSMX\n"
"XMASAMXAMM\n"
"XXAMMXXAMA\n"
"SMSMSASXSS\n"
"SAXAMASAAA\n"
"MAMMMXMMMM\n"
"MXMXAXMASX\n";

typedef struct {
    int x, y;
} vector_t;

static vector_t dirs[] = {
    {-1, -1}, {0, -1}, {1, -1},
    {-1, 0}, {1, 0},
    {-1, 1}, {0, 1}, {1, 1},
};

static long part1(const char *src) {
    assert(strchr(src, '\n'));
    int stride = strchr(src, '\n') - src + 1;
    int w = stride - 1;
    int h = strlen(src) / stride;
    int count = 0;
    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            if (src[r * stride + c] != 'X') continue;
            for (int d = 0; d < 8; ++d) {
                int matches = 1;
                for (int i = 0; i < 3; ++i) {
                    int nc = c + (i + 1) * dirs[d].x;
                    int nr = r + (i + 1) * dirs[d].y;
                    if (nc < 0 || nc >= w || nr < 0 || nr >= h || src[nr * stride + nc] != "MAS"[i]) {
                        matches = 0;
                        break;
                    }
                }
                if (matches) count++;
            }
        }
    }
    return count;
}

static long part2(const char *src) {
    assert(strchr(src, '\n'));
    int stride = strchr(src, '\n') - src + 1;
    int w = stride - 1;
    int h = strlen(src) / stride;
    int count = 0;
    for (int r = 1; r < h - 1; ++r) {
        for (int c = 1; c < w - 1; ++c) {
            if (src[r * stride + c] != 'A') continue;
            int nw = src[(r - 1) * stride + (c - 1)];
            int ne = src[(r - 1) * stride + (c + 1)];
            int sw = src[(r + 1) * stride + (c - 1)];
            int se = src[(r + 1) * stride + (c + 1)];
            if ((nw == 'M' && se == 'S' || nw == 'S' && se == 'M')
                &&
                (ne == 'M' && sw == 'S' || ne == 'S' && sw == 'M')) count++;
        }
    }
    return count;
}

int main(int argc, char *argv[]) {
    assert(part1(SAMPLE) == 18);
    assert(part2(SAMPLE) == 9);
    char *src = read_input("2024/in/04.txt");
    printf("%ld\n", part1(src));
    printf("%ld\n", part2(src));
    free(src);
}
