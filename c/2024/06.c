#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../util.h"


const char *SAMPLE =
"....#.....\n"
".........#\n"
"..........\n"
"..#.......\n"
".......#..\n"
"..........\n"
".#..^.....\n"
"........#.\n"
"#.........\n"
"......#...\n";

typedef enum {
    N, E, S, W
} dir_t;

typedef struct {
    int w, h;
    char *data;
    char *visited;
    int x, y;
    dir_t dir;
} grid_t;

static int DIRSX[] = {0, 1, 0, -1};
static int DIRSY[] = {-1, 0, 1, 0};

static void parse(const char *src, grid_t *grid) {
    int w = strchr(src, '\n') - src + 2;
    int h = strlen(src) / (w - 1) + 2;
    grid->w = w;
    grid->h = h;
    grid->data = malloc(grid->w * grid->h);
    for (int y = 0; y < h; ++y) {
        for (int x = 0; x < w; ++x) {
            if (y == 0 || y == h - 1 || x == 0 || x == w - 1) {
                grid->data[y * w + x] = '*';
            } else {
                char c = src[(y - 1) * (w - 1) + x - 1];
                switch (c) {
                    case '^':
                        grid->dir = N;
                        break;
                    case 'v':
                        grid->dir = S;
                        break;
                    case '<':
                        grid->dir = W;
                        break;
                    case '>':
                        grid->dir = E;
                        break;
                }
                if (c != '.' && c != '#') {
                    grid->x = x;
                    grid->y = y;
                }
                grid->data[y * w + x] = c;
            }
        }
    }
    grid->visited = malloc(grid->w * grid->h);
}

static void grid_print(const grid_t *grid) {
    for (int y = 0; y < grid->h; ++y) {
        for (int x = 0; x < grid->w; ++x) {
            putchar(grid->data[y * grid->w + x]);
        }
        putchar('\n');
    }
}

static int simulate_guard(const grid_t *grid) {
    memset(grid->visited, 0, grid->w * grid->h);
    int y = grid->y;
    int x = grid->x;
    dir_t dir = grid->dir;
    while (1) {
        int index = y * grid->w + x;
        if (grid->visited[index] & (1 << dir)) {
            return 0;
        }
        grid->visited[index] |= 1 << dir;
        int nx = x + DIRSX[dir];
        int ny = y + DIRSY[dir];
        index = ny * grid->w + nx;
        if (grid->data[index] == '*') {
            return 1;
        }
        if (grid->data[index] == '#') {
            dir = (dir + 1) & 3;
        } else {
            x = nx;
            y = ny;
        }
    }
}

static long part1(const char *src) {
    grid_t grid;
    parse(src, &grid);
    simulate_guard(&grid);
    int count = 0;
    for (int y = 0; y < grid.h; ++y) {
        for (int x = 0; x < grid.w; ++x) {
            if (grid.visited[y * grid.w + x]) {
                count++;
            }
        }
    }
    return count;
}

static long part2(const char *src) {
    grid_t grid;
    parse(src, &grid);
    int count = 0;
    for (int y = 0; y < grid.h; ++y) {
        for (int x = 0; x < grid.w; ++x) {
            int index = y * grid.w + x;
            if (grid.data[index] != '.') {
                continue;
            }
            grid.data[index] = '#';
            if (!simulate_guard(&grid)) {
                count++;
            }
            grid.data[index] = '.';
        }
    }
    return count;
}

int main(int argc, char *argv[]) {
    assert(part1(SAMPLE) == 41);
    assert(part2(SAMPLE) == 6);
    char *src = read_input("2024/in/06.txt");
    printf("%ld\n", part1(src));
    printf("%ld\n", part2(src));
    free(src);
}
