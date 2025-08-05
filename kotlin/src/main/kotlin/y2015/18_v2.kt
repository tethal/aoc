package y2015

import Dir
import Vec2
import java.io.File

private class Board1(private val board: List<String>) {
    val width = board[0].length
    val height = board.size
    fun isInBounds(pos: Vec2) = pos.y in board.indices && pos.x in board[0].indices
    fun get(pos: Vec2) = if (isInBounds(pos)) board[pos.y][pos.x] else ' '
    fun isAlive(pos: Vec2) = get(pos) == '#'

    fun advance(): Board1 {
        fun survives(pos: Vec2): Boolean {
            val aliveNeighbours = Dir.neighborsOf(pos).count(::isAlive)
            return when (isAlive(pos)) {
                true -> aliveNeighbours in 2..3
                false -> aliveNeighbours == 3
            }
        }
        return Board1(
            (0 until height).map { y ->
                (0 until width).map { x -> Vec2(x, y) }
                    .map { if (survives(it)) '#' else '.' }
                    .joinToString("")
            })
    }

    fun forceCorners(): Board1 {
        board.mapIndexed { y, row ->
            if (y == 0 || y == height - 1) "#" + row.substring(1, width - 1) + "#"
            else row
        }.let { return Board1(it) }
    }

    fun countAlive() = board.sumOf { row -> row.count { it == '#' } }
}

private fun run(input: List<String>, time: Int, adjustBoard: (Board1) -> Board1 = { it }): Int {
    return (1..time)
        .fold(adjustBoard(Board1(input))) { board, _ -> adjustBoard(board.advance()) }
        .countAlive()
}

private fun part1(input: List<String>, time: Int): Int {
    return run(input, time)
}

private fun part2(input: List<String>, time: Int): Int {
    return run(input, time) { it.forceCorners() }
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
