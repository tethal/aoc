package y2016

import util.Util.checkResult
import java.io.File

typealias Display = Array<BooleanArray>

sealed interface Cmd {
    fun apply(display: Display)

    data class Rect(val w: Int, val h: Int) : Cmd {
        override fun apply(display: Display) {
            for (y in 0 until h) {
                for (x in 0 until w) {
                    display[y][x] = true
                }
            }
        }
    }

    data class RotateCol(val x: Int, val amount: Int) : Cmd {
        override fun apply(display: Display) {
            val h = display.size
            val newCol = BooleanArray(h)
            for (y in 0 until h) {
                newCol[y] = display[(y - amount + h) % h][x]
            }
            for (y in 0 until h) {
                display[y][x] = newCol[y]
            }
        }
    }

    data class RotateRow(val y: Int, val amount: Int) : Cmd {
        override fun apply(display: Display) {
            val w = display[0].size
            display[y] = display[y].copyOfRange(w - amount, w) + display[y].copyOfRange(0, w - amount)
        }
    }
}

val RE = """(rect (\d+)x(\d+))|(rotate column x=(\d+) by (\d+))|(rotate row y=(\d+) by (\d+))""".toRegex()

fun parseCommand(line: String): Cmd {
    val m = RE.matchEntire(line)
    if (m != null) {
        val g = m.groupValues
        if (g[1].isNotEmpty()) {
            return Cmd.Rect(g[2].toInt(), g[3].toInt())
        } else if (g[4].isNotEmpty()) {
            return Cmd.RotateCol(g[5].toInt(), g[6].toInt())
        } else if (g[7].isNotEmpty()) {
            return Cmd.RotateRow(g[8].toInt(), g[9].toInt())
        }
    }
    throw IllegalArgumentException("Invalid command: $line")
}

private fun part1(w: Int, h: Int, src: List<String>): Int {
    val display = Array(h) { BooleanArray(w) }
    src.asSequence()
        .map(::parseCommand)
        .forEach { it.apply(display) }
    display.forEach {
        it.joinToString("") { b -> if (b) "#" else " " }.let(::println)
    }
    return display.sumOf { it.count { it } }
}


fun main() {
    val SAMPLE = """
        rect 3x2
        rotate column x=1 by 1
        rotate row y=0 by 4
        rotate column x=1 by 1
        """.trimIndent().lines()
    checkResult(part1(7, 3, SAMPLE), 6)
    val input = File("in/y2016/08.txt").readLines()
    println(part1(50, 6, input))
}
