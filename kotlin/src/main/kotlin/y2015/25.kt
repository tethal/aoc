package y2015

import java.io.File

private fun triangular(n: Int) = n * (n + 1) / 2
private val gen = generateSequence(20151125L) { it * 252533 % 33554393 }
private fun part1(row: Int, col: Int) = gen.elementAt(triangular(row + col - 2) + col - 1)

fun main() {
    check(part1(6, 6) == 27995004L)
    check(part1(2, 5) == 15514188L)

    val input = File("in/y2015/25.txt").readText()
    val (row, col) = Regex("""row (\d+), column (\d+)""").find(input)!!.destructured
    println(part1(row.toInt(), col.toInt()))
}
