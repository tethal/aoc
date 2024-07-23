package y2015

import java.io.File

private fun isNice1(s: String) =
    s.count { it in "aeiou" } >= 3 &&
            s.contains("(.)\\1".toRegex()) &&
            !s.contains("ab|cd|pq|xy".toRegex())

private fun isNice2(s: String) =
    s.contains("(..).*\\1".toRegex()) &&
            s.contains("(.).\\1".toRegex())

fun main() {
    check(isNice1("ugknbfddgicrmopn"))
    check(isNice1("aaa"))
    check(!isNice1("jchzalrnumimnmhp"))
    check(!isNice1("haegwjzuvuyypxyu"))
    check(!isNice1("dvszwmarrgswjxmb"))
    check(isNice2("qjhvhtzxzqqjkmpb"))
    check(isNice2("xxyxx"))
    check(!isNice2("uurcxstgmygtbstg"))
    check(!isNice2("ieodomkazucvgmuy"))

    val input = File("in/y2015/05.txt").readLines()
    println(input.count(::isNice1))
    println(input.count(::isNice2))
}
