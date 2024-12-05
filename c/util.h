#ifndef UTIL_H__
#define UTIL_H__

#include <assert.h>
#include <stddef.h>

typedef struct {
    char *data;
    size_t capacity;
    size_t size;
    size_t stride;
} array_list_t;

void array_list_init(array_list_t *list, size_t stride);
void array_list_free(array_list_t *list, void (*free_fn)(void *));
void *array_list_append(array_list_t *list, void *value);
void array_list_foreach(const array_list_t *list, void (*fn)(void *));
void array_list_remove_index(array_list_t *list, size_t index);

static size_t array_list_size(const array_list_t *list) {
    return list->size;
}

static void *array_list_get(const array_list_t *list, size_t index) {
    assert(index < list->size);
    return list->data + index * list->stride;
}

typedef array_list_t long_array_list_t;

void long_array_list_init(long_array_list_t *list);
void long_array_list_free(long_array_list_t *list);
void long_array_list_append(long_array_list_t *list, long value);
void long_array_list_sort(const long_array_list_t *list);
void long_array_list_print(const long_array_list_t *list);
int long_array_list_contains(const long_array_list_t *list, long value);
void long_array_list_remove_value(long_array_list_t *list, long value);

static size_t long_array_list_size(const long_array_list_t *list) {
    return array_list_size(list);
}

static void long_array_list_clear(long_array_list_t *list) {
    list->size = 0;
}

static long long_array_list_get(const long_array_list_t *list, size_t index) {
    return *(long *)array_list_get(list, index);
}

char *read_input(const char *filename);

#endif // UTIL_H__