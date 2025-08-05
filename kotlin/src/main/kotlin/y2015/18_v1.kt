package y2015

import Dir
import java.io.File

private fun isAlive(c: Char) = c == '#' || c == '*'

private fun advance(board: List<String>): List<String> {
    fun aliveNeighbors(x: Int, y: Int) = Dir.neighborsOf(x, y).map { (nx, ny) -> board[ny][nx] }.count(::isAlive)
    return board.mapIndexed { y, row ->
        row.mapIndexed { x, c ->
            when (c) {
                '#' -> if (aliveNeighbors(x, y) in 2..3) '#' else '.'
                '.' -> if (aliveNeighbors(x, y) == 3) '#' else '.'
                else -> c
            }
        }.joinToString("")
    }
}

private fun part1(input: List<String>, time: Int): Int {
    val board = buildList {
        add(" ".repeat(input[0].length + 2))
        input.forEach { add(" $it ") }
        add(" ".repeat(input[0].length + 2))
    }
    return (1..time)
        .fold(board) { acc, _ -> advance(acc) }
        .sumOf { row -> row.count(::isAlive) }
}

private fun part2(input: List<String>, time: Int): Int {
    return part1(input.mapIndexed { y, row ->
        if (y == 0 || y == input.size - 1)
            "*${row.substring(1, row.length - 1)}*"
        else
            row
    }, time)
}

fun main() {
    val sample = """
        .#.#.#
        ...##.
        #....#
        ..#...
        #.#..#
        ####..
    """.trimIndent().lines()
    check(part1(sample, 4) == 4)
    check(part2(sample, 5) == 17)

    val input = File("in/y2015/18.txt").readLines()
    println(part1(input, 100))
    println(part2(input, 100))
}
