package y2015

import java.io.File

private fun parseDimensions(s: String) = s.split("x").map(String::toInt)

private fun wrappingPaper(s: String) = parseDimensions(s).let { (l, w, h) ->
    2 * (l * w + w * h + h * l) + minOf(l * w, w * h, h * l)
}

private fun ribbon(s: String) = parseDimensions(s).let { (l, w, h) ->
    2 * minOf(l + w, w + h, l + h) + l * w * h
}

fun main() {
    check(wrappingPaper("2x3x4") == 58)
    check(wrappingPaper("1x1x10") == 43)
    check(ribbon("2x3x4") == 34)
    check(ribbon("1x1x10") == 14)

    val input = File("in/y2015/02.txt").readLines()
    println(input.sumOf(::wrappingPaper))
    println(input.sumOf(::ribbon))
}
