package y2015

import Dir
import Rect
import Vec2
import java.io.File

private class Board2(private val data: Set<Vec2>, val width: Int, val height: Int) {
    fun isAlive(pos: Vec2) = data.contains(pos)
    fun countAlive() = data.size
    fun withAlive(cells: Sequence<Vec2>) = Board2(data + cells, width, height)

    fun survives(pos: Vec2): Boolean {
        val aliveNeighbours = Dir.neighborsOf(pos).count(::isAlive)
        return when (isAlive(pos)) {
            true -> aliveNeighbours in 2..3
            false -> aliveNeighbours == 3
        }
    }

    fun advance() = Board2(Rect.ofSize(width, height).points().filter(::survives).toSet(), width, height)

    companion object {
        fun from(input: List<String>) = Board2(
            input.flatMapIndexed { y, row ->
                row.mapIndexedNotNull { x, c -> if (c == '#') Vec2(x, y) else null }
            }.toSet(), input[0].length, input.size
        )
    }
}

private fun run(input: List<String>, time: Int, adjustBoard: (Board2) -> Board2 = { it }): Int {
    return (1..time)
        .fold(adjustBoard(Board2.from(input))) { board, _ -> adjustBoard(board.advance()) }
        .countAlive()
}

private fun part1(input: List<String>, time: Int): Int {
    return run(input, time)
}

private fun part2(input: List<String>, time: Int): Int {
    return run(input, time) { it.withAlive(Rect.ofSize(it.width, it.height).corners()) }
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
