package y2015

import java.io.File
import java.security.MessageDigest

private fun md5(input: String) =
    MessageDigest.getInstance("MD5")
        .digest(input.toByteArray())
        .joinToString("") { "%02x".format(it) }

private fun mine(prefix: String, expectedZeros: String) =
    (1..Int.MAX_VALUE).first { md5("$prefix$it").startsWith(expectedZeros) }

private fun part1(input: String) = mine(input, "00000")
private fun part2(input: String) = mine(input, "000000")

fun main() {
    check(part1("abcdef") == 609043)
    check(part1("pqrstuv") == 1048970)

    val input = File("in/y2015/04.txt").readText()
    println(part1(input))
    println(part2(input))
}
