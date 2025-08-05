package y2015

import java.io.File

val requirements = """
    children: 3
    cats: 7
    samoyeds: 2
    pomeranians: 3
    akitas: 0
    vizslas: 0
    goldfish: 5
    trees: 3
    cars: 2
    perfumes: 1
""".trimIndent().lines().associate {
    val (k, v) = it.split(": ")
    k to v.toInt()
}

data class Aunt(
    val id: Int,
    val properties: Map<String, Int>
)

private fun parseAunt(s: String): Aunt {
    val (id, props) = "Sue (\\d+): (.+)".toRegex().matchEntire(s)!!.destructured
    return Aunt(id.toInt(), props.split(", ").associate {
        val (k, v) = it.split(": ")
        k to v.toInt()
    })
}

private fun part1(input: List<String>) =
    input
        .map(::parseAunt)
        .first { aunt -> aunt.properties.all { (k, v) -> requirements[k] == v } }
        .id

private fun part2(input: List<String>) =
    input
        .map(::parseAunt)
        .first { aunt ->
            aunt.properties.all { (k, v) ->
                when (k) {
                    "cats", "trees" -> v > requirements[k]!!
                    "pomeranians", "goldfish" -> v < requirements[k]!!
                    else -> requirements[k] == v
                }
            }
        }
        .id

fun main() {
    val input = File("in/y2015/16.txt").readLines()
    println(part1(input))
    println(part2(input))
}
