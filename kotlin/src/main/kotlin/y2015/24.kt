package y2015

import java.io.File

private fun calc(input: List<Long>, divider: Int): Long {

    fun findGroups(packages: List<Long>, used: List<Long>, remaining: Long): List<List<Long>> {
        if (remaining == 0L) return listOf(used)
        if (packages.isEmpty() || remaining < 0) return emptyList()
        val head = packages.first()
        val tail = packages.drop(1)
        return findGroups(tail, used + head, remaining - head) + findGroups(tail, used, remaining)
    }

    val groups = findGroups(input, emptyList(), input.sum() / divider)
    val minLen = groups.minOfOrNull { it.size } ?: 0
    val minGroups = groups.filter { it.size == minLen }

    return minGroups.map { it.fold(1L) { acc, i -> acc * i } }.minOrNull() ?: 0L
}

fun main() {
    val sample = listOf(1L, 2L, 3L, 4L, 5L, 7L, 8L, 9L, 10L, 11L)
    check(calc(sample, 3) == 99L)
    check(calc(sample, 4) == 44L)

    val input = File("in/y2015/24.txt").readLines().map(String::toLong)
    println(calc(input, 3))
    println(calc(input, 4))
}