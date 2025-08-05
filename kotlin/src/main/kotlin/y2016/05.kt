package y2016

import java.security.MessageDigest

private fun part1(idStr: String): String {
    val sb = StringBuilder();
    for (i in 0..Int.MAX_VALUE) {
        val hash = (idStr + i).md5()
        if (hash != null) {
            sb.append(hash)
        }
        if (sb.length == 8) break

    }

    return sb.toString()
}

val md = MessageDigest.getInstance("MD5")
val HEX = "0123456789abcdef"

fun String.md5(): Char? {
    val digest = md.digest(toByteArray())
    if (digest[0].toInt() == 0 && digest[1].toInt() == 0 && (digest[2].toInt() and 0xf0) == 0) {
        return "0123456789ABCDEF"[digest[2].toInt() and 0x0f]
    }
    return null
}

fun main() {
    println(part1("abc"))
//    println(part1(input))
}
