package y2015

import Dir
import Vec2
import java.io.File

private fun getHousesOnPath(path: String, filter: (Int) -> Boolean = { true }) =
    path
        .asSequence()
        .filterIndexed { i, _ -> filter(i) }
        .map(Dir::fromArrowChar)
        .runningFold(Vec2.ZERO) { acc, d -> acc + d }
        .toSet()

private fun part1(input: String) =
    getHousesOnPath(input).size

private fun part2(input: String) =
    (getHousesOnPath(input) { it and 1 == 0 } + getHousesOnPath(input) { it and 1 == 1 }).size

fun main() {
    check(part1(">") == 2)
    check(part1("^>v<") == 4)
    check(part1("^v^v^v^v^v") == 2)
    check(part2("^v") == 3)
    check(part2("^>v<") == 3)
    check(part2("^v^v^v^v^v") == 11)

    val input = File("in/y2015/03.txt").readText()
    println(part1(input))
    println(part2(input))
}
