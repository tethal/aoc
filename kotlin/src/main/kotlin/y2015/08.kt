package y2015

import java.io.File

private fun countDiff(s: String): Int {
    var diff = 2
    var i = 1
    while (i < s.length - 1) {
        if (s[i++] == '\\') {
            if (s[i] == 'x') {
                i += 2
                diff += 2
            }
            diff++
            i++
        }
    }
    return diff
}

private fun countDiff2(s: String): Int {
    return s.count { it == '\\' || it == '"' } + 2
}

fun main() {
    val sample = """
        ""
        "abc"
        "aaa\"aaa"
        "\x27"
    """.trimIndent().lines()
    check(sample.sumOf(::countDiff) == 12)
    sample.forEach { println(countDiff2(it)) }
    check(sample.sumOf(::countDiff2) == 19)

    val input = File("in/y2015/08.txt").readLines()
    println(input.sumOf(::countDiff))
    println(input.sumOf(::countDiff2))
}