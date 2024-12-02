#include "util.h"

#include <stdio.h>
#include <stdlib.h>

static int cmp_long(const void *a, const void *b) {
    return *(long *)a - *(long *)b;
}

void long_array_list_init(long_array_list_t *list) {
    size_t capacity = 8;
    list->data = malloc(sizeof(long) * capacity);
    assert(list->data);
    list->capacity = capacity;
    list->size = 0;
}

void long_array_list_free(long_array_list_t *list) {
    free(list->data);
    list->data = NULL;
    list->capacity = 0;
    list->size = 0;
}

void long_array_list_append(long_array_list_t *list, long value) {
    if (list->size == list->capacity) {
        list->capacity *= 2;
        list->data = realloc(list->data, sizeof(long) * list->capacity);
        assert(list->data);
    }
    list->data[list->size++] = value;
}

void long_array_list_sort(const long_array_list_t *list) {
    qsort(list->data, list->size, sizeof(long), cmp_long);
}

void long_array_list_print(const long_array_list_t *list) {
    for (size_t i = 0; i < list->size; i++) {
        printf("%ld ", list->data[i]);
    }
    printf("\n");
}

char *read_input(const char *filename) {
    FILE *f = fopen(filename, "r");
    assert(f);
    fseek(f, 0, SEEK_END);
    long size = ftell(f);
    fseek(f, 0, SEEK_SET);
    char *src = malloc(size + 1);
    assert(src);
    size_t read = fread(src, size, 1, f);
    assert(read == 1);
    src[size] = '\0';
    fclose(f);
    return src;
}
