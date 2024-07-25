package y2015

import Rect
import java.io.File

private enum class Action {
    ON, OFF, TOGGLE
}

private data class Instruction2(val action: Action, val rect: Rect)

private fun parse(s: String): Instruction2 {
    "(.*) (\\d+),(\\d+) through (\\d+),(\\d+)".toRegex().matchEntire(s).let { match ->
        val (a, x1, y1, x2, y2) = match!!.destructured
        val action = when (a) {
            "turn on" -> Action.ON
            "turn off" -> Action.OFF
            "toggle" -> Action.TOGGLE
            else -> throw IllegalArgumentException()
        }
        return Instruction2(action, Rect.fromCorners(x1.toInt(), y1.toInt(), x2.toInt(), y2.toInt()))
    }
}

private fun executeInstructions(input: List<String>, actionHandler: (Action, Int) -> Int): Int {
    val w = 1000
    val h = 1000
    val map = IntArray(w * h)
    input.map(::parse).forEach { (action, rect) ->
        rect.points().map { it.y * w + it.x }.forEach { i ->
            map[i] = actionHandler(action, map[i])
        }
    }
    return map.sum()
}

private fun part1(action: Action, value: Int) =
    when (action) {
        Action.ON -> 1
        Action.OFF -> 0
        Action.TOGGLE -> 1 - value
    }

private fun part2(action: Action, value: Int) =
    when (action) {
        Action.ON -> value + 1
        Action.OFF -> maxOf(0, value - 1)
        Action.TOGGLE -> value + 2
    }

fun main() {
    val input = File("in/y2015/06.txt").readLines()
    println(executeInstructions(input, ::part1))
    println(executeInstructions(input, ::part2))
}
