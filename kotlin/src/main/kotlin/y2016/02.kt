package y2016

import java.io.File

private fun part1(s: String) =
    s.lines().runningFold(5) { pos, line ->
        line.fold(pos) { p, c -> "124123513362157426843695487759876998"[(p - 1) * 4 + "URDL".indexOf(c)].digitToInt() }
    }.drop(1).joinToString("")


fun main() {
    val str = "qwefjbqkfcnqef";
    val letters = str.replace("-", "").groupingBy { it }.eachCount()

    check(part1("ULL\nRRDDD\nLURDL\nUUUUD") == "1985")

    "".md5()

    val input = File("in/y2016/02.txt").readText()
    println(part1(input))
}
