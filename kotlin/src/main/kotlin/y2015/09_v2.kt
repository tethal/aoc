package y2015

import permutations
import java.io.File

private fun solve(input: List<String>, f: (Int, Int) -> Int): Int {
    val distances = mutableMapOf<Pair<String, String>, Int>()
    input
        .map { it.split(" to ", " = ") }
        .forEach { (a, b, d) ->
            distances[a to b] = d.toInt()
            distances[b to a] = d.toInt()
        }

    val allCities = distances.keys.map { it.second }.toSet()
    fun pathLength(path: List<String>) = path.zipWithNext().sumOf { (a, b) -> distances[a to b]!! }

    return permutations(allCities).map(::pathLength).reduce(f)
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

data class Node(val name: String, val neighbors: List<Pair<Node, Int>>) {
    fun visit(pathSoFar: List<Node>) {
        for (n in neighbors) {
            if (n.first !in pathSoFar) {
                n.first.visit(pathSoFar + n.first)
            }
        }
    }
}

