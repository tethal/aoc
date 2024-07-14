package y2015

import java.io.File

private fun part1(input: String) =
    input
        .asSequence()
        .map { if (it == '(') 1 else -1 }
        .sum()

private fun part2(input: String) =
    input
        .asSequence()
        .map { if (it == '(') 1 else -1 }
        .runningFold(0, Int::plus)
        .indexOf(-1)

private fun part1x(input: String): Int {
    if (!input.contains(')')) return input.length
    if (!input.contains('(')) return -input.length
    return part1x(input.replace("()", "").replace(")(", ""))
}

private fun part1y(input: String) =
    input.length - 2 * input.count { it == ')' }

fun main() {
    check(part1("(())") == 0)
    check(part1(")())())") == -3)
    check(part2(")") == 1)
    check(part2("()())") == 5)

    val input = File("in/y2015/01.txt").readText()
    println(part1(input))
    println(part2(input))
}
