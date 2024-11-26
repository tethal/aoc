package y2015

import java.io.File

private fun solve(input: List<String>, f: (Int, Int) -> Int): Int {
    val distances = mutableMapOf<Pair<String, String>, Int>()
    input
        .map { it.split(" to ", " = ") }
        .forEach { (a, b, d) ->
            distances[a to b] = d.toInt()
            distances[b to a] = d.toInt()
        }
    distances.keys.map { it.first }.forEach { city ->
        distances["" to city] = 0
    }

    fun findPath(start: String, remainingCities: Set<String>): Int {
        if (remainingCities.isEmpty()) return 0
        return remainingCities.map { city ->
            distances[start to city]!! + findPath(city, remainingCities - city)
        }.reduce(f)
    }

    return findPath("", distances.keys.map { it.second }.toSet())
}

fun main() {
    val sample = """
        London to Dublin = 464
        London to Belfast = 518
        Dublin to Belfast = 141
    """.trimIndent().lines()
    check(solve(sample, Math::min) == 605)
    check(solve(sample, Math::max) == 982)

    val input = File("in/y2015/09.txt").readLines()
    println(solve(input, Math::min))
    println(solve(input, Math::max))
}
