package y2015

import java.io.File

private fun solve(input: List<String>, part2: Boolean): Int {
    val ingredients = input.map {
        val (capacity, durability, flavor, texture, calories) = "capacity (-?\\d+), durability (-?\\d+), flavor (-?\\d+), texture (-?\\d+), calories (-?\\d+)".toRegex()
            .find(it)!!.destructured
        listOf(capacity.toInt(), durability.toInt(), flavor.toInt(), texture.toInt(), calories.toInt())
    }

    fun score(quantities: List<Int>): Int {
        if (part2 && ingredients.zip(quantities).sumOf { (i, q) -> q * i.last() } != 500) return 0
        return (0 until 4)
            .map { attr -> ingredients.zip(quantities).sumOf { (i, q) -> i[attr] * q } }
            .map { 0.coerceAtLeast(it) }
            .reduce(Int::times)
    }

    fun findMaxScore(remaining: Int, quantities: List<Int>): Int {
        if (quantities.size + 1 == ingredients.size) return score(quantities + remaining)
        if (remaining <= 1) return 0
        return (1..<remaining).maxOf { i -> findMaxScore(remaining - i, quantities + i) }
    }

    return findMaxScore(100, emptyList())
}

fun main() {
    val sample = """
        Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
        Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
    """.trimIndent().lines()
    check(solve(sample, false) == 62842880)
    check(solve(sample, true) == 57600000)

    val input = File("in/y2015/15.txt").readLines()
    println(solve(input, false))
    println(solve(input, true))
}