package y2015

import java.io.File

private data class Instruction(val action: String, val startX: Int, val startY: Int, val endX: Int, val endY: Int)

private fun parse(s: String): Instruction {
    "(.*) (\\d+),(\\d+) through (\\d+),(\\d+)".toRegex().matchEntire(s).let { match ->
        val (action, x1, y1, x2, y2) = match!!.destructured
        return Instruction(action, x1.toInt(), y1.toInt(), x2.toInt(), y2.toInt())
    }
}

private fun executeInstructions(input: List<String>, actionHandler: (String, Int) -> Int): Int {
    val w = 1000
    val h = 1000
    val grid = Array(h) { IntArray(w) }
    input.map(::parse).forEach { (action, startX, startY, endX, endY) ->
        for (x in startX..endX) {
            for (y in startY..endY) {
                grid[y][x] = actionHandler(action, grid[y][x])
            }
        }
    }
    return grid.sumOf { it.sum() }
}

private fun part1(input: List<String>): Int {
    return executeInstructions(input) { action, value ->
        when (action) {
            "turn on" -> 1
            "turn off" -> 0
            "toggle" -> 1 - value
            else -> throw IllegalArgumentException()
        }
    }
}

private fun part2(input: List<String>): Int {
    return executeInstructions(input) { action, value ->
        when (action) {
            "turn on" -> value + 1
            "turn off" -> maxOf(0, value - 1)
            "toggle" -> value + 2
            else -> throw IllegalArgumentException()
        }
    }
}

fun main() {
    val input = File("in/y2015/06.txt").readLines()
    println(part1(input))
    println(part2(input))
}
