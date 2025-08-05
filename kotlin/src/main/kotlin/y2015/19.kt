package y2015

import java.io.File

private fun part1(input: List<String>): Int {
    val replacements = input.takeWhile { it.isNotEmpty() }.map { it.split(" => ") }
    val molecule = input.last()
    val molecules = mutableSetOf<String>()
    for ((from, to) in replacements) {
        var i = 0
        while (i < molecule.length) {
            val j = molecule.indexOf(from, i)
            if (j == -1) break
            molecules.add(molecule.substring(0, j) + to + molecule.substring(j + from.length))
            i = j + 1
        }
    }
    return molecules.toSet().size
}

private fun part2(input: List<String>): Int {
    val replacements =
        input
            .takeWhile { it.isNotEmpty() }
            .map { it.split(" => ") }
            .map { (from, to) -> from.reversed() to to.reversed() }
    val re = replacements.joinToString("|") { it.second }.toRegex()
    var steps = 0
    var molecule = input.last().reversed()
    while (molecule != "e") {
        val rhs = re.find(molecule)!!.value
        val lhs = replacements.first { rhs == it.second }.first
        molecule = molecule.replaceFirst(rhs, lhs)
        ++steps
    }
    return steps
}

fun main() {
    val sample = """
        e => H
        e => O
        H => HO
        H => OH
        O => HH
        
        HOH
    """.trimIndent().lines()
    check(part1(sample) == 4)

    val input = File("in/y2015/19.txt").readLines()
    println(part1(input))
    println(part2(input))
}
