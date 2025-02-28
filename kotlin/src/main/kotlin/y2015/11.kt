package y2015

import java.io.File

private fun isValid(s: String): Boolean {
    val hasStraight = s.windowed(3).any { it[2] == it[1] + 1 && it[1] == it[0] + 1 }
    val hasForbidden = s.any { it == 'i' || it == 'o' || it == 'l' }
    var pairCount = 0
    var i = 0
    while (i < s.length - 1) {
        if (s[i] == s[i + 1]) {
            pairCount++
            i += 2
        } else {
            i++
        }
    }
    return hasStraight && !hasForbidden && pairCount >= 2
}

private fun increment(s: String): String {
    val sb = StringBuilder(s)
    var i = s.length - 1
    while (i >= 0) {
        if (s[i] == 'z') {
            sb[i] = 'a'
            i--
        } else {
            sb[i] = s[i] + 1
            break
        }
    }
    return sb.toString()
}

private fun next(s: String) = generateSequence(s, ::increment).drop(1).filter(::isValid).first()

fun main() {
    check(!isValid("hijklmmn"))
    check(!isValid("abbceffg"))
    check(!isValid("abbcegjk"))
    check(isValid("abcdffaa"))
    check(isValid("ghjaabcc"))
    check(next("abcdefgh") == "abcdffaa")
    check(next("ghijklmn") == "ghjaabcc")

    val input = File("in/y2015/11.txt").readText().trim()
    println(next(input))
    println(next(next(input)))
}
