package y2015

import java.io.File

private fun lookAndSay(s: String): String {
    val sb = StringBuilder()
    var i = 0
    while (i < s.length) {
        var count = 1
        while (i + 1 < s.length && s[i] == s[i + 1]) {
            i++
            count++
        }
        sb.append(count).append(s[i])
        i++
    }
    return sb.toString()
}

private fun iterate(s: String, n: Int): String {
    var result = s
    repeat(n) {
        result = lookAndSay(result)
    }
    return result
}

fun main() {
    check(lookAndSay("1") == "11")
    check(lookAndSay("11") == "21")
    check(lookAndSay("21") == "1211")
    check(lookAndSay("1211") == "111221")
    check(lookAndSay("111221") == "312211")

    val input = File("in/y2015/10.txt").readText().trim()
    println(iterate(input, 40).length)
    println(iterate(input, 50).length)
}
