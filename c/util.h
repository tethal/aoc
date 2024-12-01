#ifndef UTIL_H__
#define UTIL_H__

#include <assert.h>
#include <stddef.h>

typedef struct {
    long *data;
    size_t capacity;
    size_t size;
} long_array_list_t;

void long_array_list_init(long_array_list_t *list);
void long_array_list_free(long_array_list_t *list);
void long_array_list_append(long_array_list_t *list, long value);
void long_array_list_sort(const long_array_list_t *list);

static size_t long_array_list_size(const long_array_list_t *list) {
    return list->size;
}

static long long_array_list_get(const long_array_list_t *list, size_t index) {
    assert(index < list->size);
    return list->data[index];
}

char *read_input(const char *filename);

#endif // UTIL_H__