package y2015

import java.io.File

private fun calc(target: Int, multiplier: Int, max: Int): Int {
    val houses = IntArray(target / multiplier)
    for (elf in 1 until houses.size) {
        var i = 1
        while (i < max && i * elf < houses.size) {
            houses[i * elf] += elf * multiplier
            ++i
        }
    }
    return houses.indexOfFirst { it >= target }
}

private fun part1(target: Int) = calc(target, 10, Int.MAX_VALUE)
private fun part2(target: Int) = calc(target, 11, 50)

fun main() {
    check(part1(110) == 6)

    val input = File("in/y2015/20.txt").readText().trim().toInt()
    println(part1(input))
    println(part2(input))
}
