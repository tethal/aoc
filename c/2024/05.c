#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../util.h"


const char *SAMPLE =
"47|53\n"
"97|13\n"
"97|61\n"
"97|47\n"
"75|29\n"
"61|13\n"
"75|53\n"
"29|13\n"
"97|29\n"
"53|29\n"
"61|53\n"
"97|53\n"
"61|29\n"
"47|13\n"
"75|47\n"
"97|75\n"
"47|61\n"
"75|61\n"
"47|29\n"
"75|13\n"
"53|13\n"
"\n"
"75,47,61,53,29\n"
"97,61,53,29,13\n"
"75,29,13\n"
"75,97,47,61,53\n"
"61,13,29\n"
"97,13,75,29,47\n";

typedef struct {
    long a, b;
} rule_t;

typedef struct {
    array_list_t rules;
    long_array_list_t updates;
} data_t;

static void rule_print(void *e) {
    rule_t *rule = e;
    printf("%ld %ld\n", rule->a, rule->b);
}

static void data_print(const data_t *data) {
    array_list_foreach(&data->rules, rule_print);
    array_list_foreach(&data->updates, (void (*)(void *)) long_array_list_print);
}

static void data_parse(data_t *data, const char *src) {
    array_list_init(&data->rules, sizeof(rule_t));
    while (*src != '\n') {
        char *p;
        rule_t *rule = array_list_append(&data->rules, NULL);
        rule->a = strtol(src, &p, 10);
        rule->b = strtol(p + 1, &p, 10);
        src = p + 1;
    }

    array_list_init(&data->updates, sizeof(long_array_list_t));
    src++;
    while (*src) {
        long_array_list_t *update = array_list_append(&data->updates, NULL);
        long_array_list_init(update);
        while (1) {
            char *p;
            long_array_list_append(update, strtol(src, &p, 10));
            src = p + 1;
            if (*p == '\n') {
                break;
            }
        }
    }
}

static void data_free(data_t *data) {
    array_list_free(&data->rules, NULL);
    array_list_free(&data->updates, (void (*)(void *)) long_array_list_free);
}

static long middle(const long_array_list_t *update) {
    return long_array_list_get(update, long_array_list_size(update) / 2);
}

static int check_rules(const long_array_list_t *update, const array_list_t *rules) {
    for (size_t i = 0; i < long_array_list_size(update); ++i) {
        long page = long_array_list_get(update, i);
        for (size_t j = 0; j < array_list_size(rules); ++j) {
            const rule_t *rule = array_list_get(rules, j);
            if (rule->a == page) {
                for (size_t k = 0; k < i; ++k) {
                    if (long_array_list_get(update, k) == rule->b) {
                        return 0;
                    }
                }
            }
        }
    }
    return 1;
}

static long part1(const char *src) {
    data_t data;
    data_parse(&data, src);

    long result = 0;
    for (size_t i = 0; i < array_list_size(&data.updates); ++i) {
        long_array_list_t *update = array_list_get(&data.updates, i);
        if (check_rules(update, &data.rules)) {
            result += middle(update);
        }
    }

    data_free(&data);
    return result;
}

static void visit(long page, long_array_list_t *todo, const array_list_t *rules, long_array_list_t *result, long_array_list_t *visited) {
    if (!long_array_list_contains(todo, page)) {
        return;
    }
    assert(!long_array_list_contains(visited, page));
    long_array_list_append(visited, page);
    for (size_t i = 0; i < array_list_size(rules); ++i) {
        const rule_t *rule = array_list_get(rules, i);
        if (rule->a == page) {
            visit(rule->b, todo, rules, result, visited);
        }
    }
    long_array_list_remove_value(todo, page);
    long_array_list_append(result, page);
}

static long topo_sort(long_array_list_t *todo, const array_list_t *rules) {
    long_array_list_t result;
    long_array_list_init(&result);
    long_array_list_t visited;
    long_array_list_init(&visited);

    while (long_array_list_size(todo)) {
        visit(long_array_list_get(todo, 0), todo, rules, &result, &visited);
    }

    long m = middle(&result);
    long_array_list_free(&result);
    long_array_list_free(&visited);
    return m;
}

static long part2(const char *src) {
    data_t data;
    data_parse(&data, src);

    long result = 0;
    for (size_t i = 0; i < array_list_size(&data.updates); ++i) {
        long_array_list_t *update = array_list_get(&data.updates, i);
        if (check_rules(update, &data.rules)) {
            continue;
        }
        result += topo_sort(update, &data.rules);
    }

    data_free(&data);
    return result;
}

int main(int argc, char *argv[]) {
    assert(part1(SAMPLE) == 143);
    assert(part2(SAMPLE) == 123);
    char *src = read_input("2024/in/05.txt");
    printf("%ld\n", part1(src));
    printf("%ld\n", part2(src));
    free(src);
}
