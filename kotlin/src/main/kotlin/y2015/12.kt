package y2015

import java.io.File

private fun part1(input: String): Int {
    val regex = Regex("""(-?\d+)""")
    return regex.findAll(input).sumOf { it.value.toInt() }
}

private fun part2(input: String): Int {
    var s = input
    while (true) {
        val red = s.indexOf(":\"red\"")
        if (red == -1) break
        var i = red
        var depth = 1
        while (i >= 0) {
            if (s[i] == '}') depth++
            if (s[i] == '{') depth--
            if (depth == 0) break
            i--
        }
        var j = red
        depth = 1
        while (j < s.length) {
            if (s[j] == '{') depth++
            if (s[j] == '}') depth--
            if (depth == 0) break
            j++
        }
        s = s.substring(0, i) + s.substring(j + 1)
    }
    return part1(s)
}

fun main() {
    check(part1("[1,2,3]").toString() == "6")
    check(part1("""{"a":2,"b":4}""").toString() == "6")
    check(part1("""[[[3]]]""").toString() == "3")
    check(part1("""{"a":{"b":4},"c":-1}""").toString() == "3")
    check(part1("""{"a":[-1,1]}""").toString() == "0")
    check(part1("""[-1,{"a":1}]""").toString() == "0")
    check(part1("""[]""").toString() == "0")
    check(part1("""{}""").toString() == "0")
    check(part2("""[1,2,3]""").toString() == "6")
    check(part2("""[1,{"c":"red","b":2},3]""").toString() == "4")
    check(part2("""{"d":"red","e":[1,2,3,4],"f":5}""").toString() == "0")
    check(part2("""[1,"red",5]""").toString() == "6")

    val input = File("in/y2015/12.txt").readText()
    println(part1(input))
    println(part2(input))
}
