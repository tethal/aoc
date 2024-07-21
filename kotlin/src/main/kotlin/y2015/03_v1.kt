package y2015

import java.io.File

private fun getHousesOnPath(path: String) =
    path.asSequence().runningFold(0 to 0) { (x, y), c ->
        when (c) {
            '^' -> x to y + 1
            'v' -> x to y - 1
            '<' -> x - 1 to y
            '>' -> x + 1 to y
            else -> throw IllegalArgumentException()
        }
    }.toSet()

private fun part1(input: String) = getHousesOnPath(input).size
private fun part2(input: String): Int {
    val santaPath = input.filterIndexed { i, _ -> i and 1 == 0 }
    val roboPath = input.filterIndexed { i, _ -> i and 1 == 1 }
    return (getHousesOnPath(santaPath) + getHousesOnPath(roboPath)).size
}

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
