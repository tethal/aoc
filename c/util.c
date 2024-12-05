#include "util.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void array_list_init(array_list_t *list, size_t stride) {
    size_t capacity = 8;
    list->data = malloc(stride * capacity);
    assert(list->data);
    list->capacity = capacity;
    list->size = 0;
    list->stride = stride;
}

void array_list_free(array_list_t *list, void (*free_fn)(void *)) {
    if (free_fn) {
        array_list_foreach(list, free_fn);
    }
    free(list->data);
    list->data = NULL;
    list->capacity = 0;
    list->size = 0;
    list->stride = 0;
}

void *array_list_append(array_list_t *list, void *value) {
    if (list->size == list->capacity) {
        list->capacity *= 2;
        list->data = realloc(list->data, list->stride * list->capacity);
        assert(list->data);
    }
    void *dst = list->data + list->stride * list->size++;
    if (value) {
        memcpy(dst, value, list->stride);
    }
    return dst;
}

void array_list_foreach(const array_list_t *list, void (*fn)(void *)) {
    for (size_t i = 0; i < list->size; i++) {
        fn(array_list_get(list, i));
    }
}

void array_list_remove_index(array_list_t *list, size_t index) {
    assert(index < list->size);
    list->size--;
    if (index < list->size) {
        memmove(list->data + index * list->stride, list->data + (index + 1) * list->stride, list->stride * (list->size - index));
    }
}


static int cmp_long(const void *a, const void *b) {
    return *(long *)a - *(long *)b;
}

void long_array_list_init(long_array_list_t *list) {
    array_list_init(list, sizeof(long));
}

void long_array_list_free(long_array_list_t *list) {
    array_list_free(list, NULL);
}

void long_array_list_append(long_array_list_t *list, long value) {
    array_list_append(list, &value);
}

void long_array_list_sort(const long_array_list_t *list) {
    qsort(list->data, list->size, sizeof(long), cmp_long);
}

static void print_long(void *value) {
    printf("%ld ", *(long *) value);
}

void long_array_list_print(const long_array_list_t *list) {
    array_list_foreach(list, print_long);
    printf("\n");
}

int long_array_list_contains(const long_array_list_t *list, long value) {
    for (size_t i = 0; i < long_array_list_size(list); ++i) {
        if (long_array_list_get(list, i) == value) {
            return 1;
        }
    }
    return 0;
}

void long_array_list_remove_value(long_array_list_t *list, long value) {
    for (size_t i = 0; i < long_array_list_size(list); ++i) {
        if (long_array_list_get(list, i) == value) {
            array_list_remove_index(list, i);
            return;
        }
    }
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
