#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

#include "../util.h"

const char *SAMPLE = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))";
const char *SAMPLE2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))";

typedef enum {
    S_INIT,
    S_M, S_MU, S_MUL, S_MUL_LPAREN, S_MUL_A, S_MUL_COMMA, S_MUL_B,
    S_D, S_DO, S_DO_LPAREN, S_DON, S_DON_AP, S_DONT, S_DONT_LPAREN,
} state_t;

static const char *parse(const char *src, long *a, long *b, int part2) {
    state_t state = S_INIT;
    while (*src) {
        char c = *src++;
        switch (state) {
            case S_INIT: if (c == 'm') { state = S_M; } else if (c == 'd' && part2) { state = S_D; } break;
            case S_M: if (c == 'u') { state = S_MU; } else { state = S_INIT; } break;
            case S_MU: if (c == 'l') { state = S_MUL; } else { state = S_INIT; } break;
            case S_MUL: if (c == '(') { state = S_MUL_LPAREN; *a = 0; *b = 0; } else { state = S_INIT; } break;
            case S_MUL_LPAREN: if (isdigit(c)) { state = S_MUL_A; *a = *a * 10 + c - '0'; } else { state = S_INIT; } break;
            case S_MUL_A: if (isdigit(c)) { *a = *a * 10 + c - '0'; } else if (c == ',') { state = S_MUL_COMMA; } else { state = S_INIT; } break;
            case S_MUL_COMMA: if (isdigit(c)) { state = S_MUL_B; *b = *b * 10 + c - '0'; } else { state = S_INIT; } break;
            case S_MUL_B: if (isdigit(c)) { *b = *b * 10 + c - '0'; } else if (c == ')') { return src; } else { state = S_INIT; } break;
            case S_D: if (c == 'o') { state = S_DO; } else { state = S_INIT; } break;
            case S_DO: if (c == '(') { state = S_DO_LPAREN; } else if (c == 'n') { state = S_DON; } else { state = S_INIT; } break;
            case S_DO_LPAREN: if (c == ')') { *a = -2; *b = 1; return src; } else { state = S_INIT; } break;
            case S_DON: if (c == '\'') { state = S_DON_AP; } else { state = S_INIT; } break;
            case S_DON_AP: if (c == 't') { state = S_DONT; } else { state = S_INIT; } break;
            case S_DONT: if (c == '(') { state = S_DONT_LPAREN; } else { state = S_INIT; } break;
            case S_DONT_LPAREN: if (c == ')') { *a = -2; *b = 0; return src; } else { state = S_INIT; } break;
        }
    }
    *a = -1;
    return src;
}

static long part1(const char *src) {
    long sum = 0;
    while (1) {
        long a, b;
        src = parse(src, &a, &b, 0);
        if (a < 0) {
            return sum;
        }
        sum += a * b;
    }
}

static long part2(const char *src) {
    long sum = 0;
    long enabled = 1;
    while (1) {
        long a, b;
        src = parse(src, &a, &b, 1);
        if (a == -2) {
            enabled = b;
        } else if (a < 0) {
            return sum;
        } else if (enabled) {
            sum += a * b;
        }
    }
}

int main(int argc, char *argv[]) {
    assert(part1(SAMPLE) == 161);
    assert(part2(SAMPLE2) == 48);
    char *src = read_input("2024/in/03.txt");
    printf("%ld\n", part1(src));
    printf("%ld\n", part2(src));
    free(src);
}
