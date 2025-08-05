package y2015

import java.io.File

private fun part1(total: Int, containers: List<Int>): Int {
    if (total == 0) return 1
    if (total < 0 || containers.isEmpty()) return 0
    return part1(total, containers.drop(1)) + part1(total - containers.first(), containers.drop(1))
}

private fun part2(total: Int, containers: List<Int>): Int {

    var shortestLen = containers.size + 1
    var shortestCount = 0

    fun findShortest(total: Int, containers: List<Int>, len: Int) {
        if (total == 0) {
            if (len < shortestLen) {
                shortestLen = len
                shortestCount = 1
            } else if (len == shortestLen) {
                shortestCount++
            }
            return
        }
        if (total < 0 || containers.isEmpty()) return
        findShortest(total, containers.drop(1), len)
        findShortest(total - containers.first(), containers.drop(1), len + 1)
    }

    findShortest(total, containers, 0)
    return shortestCount
}

fun main() {
    check(part1(25, listOf(20, 15, 10, 5, 5)) == 4)
    check(part2(25, listOf(20, 15, 10, 5, 5)) == 3)

    val input = File("in/y2015/17.txt").readLines().map(String::toInt)
    println(part1(150, input))
    println(part2(150, input))
}
