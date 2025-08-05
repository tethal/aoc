package y2015

import java.io.File

private fun parse(s: String): Pair<Pair<String, String>, Int> {
    val (a, b, c, d) = Regex("""(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).""").matchEntire(
        s
    )!!.destructured
    return Pair(Pair(a, d), if (b == "gain") c.toInt() else -c.toInt())
}

private fun calc(happiness: (a: String, b: String) -> Int, first: String, others: Set<String>): Int {
    fun bestHappiness(last: String, others: Set<String>, seatedHappiness: Int): Int {
        if (others.isEmpty()) {
            return seatedHappiness + happiness(last, first) + happiness(first, last)
        }
        return others.maxOf { next ->
            val newHappiness = seatedHappiness + happiness(last, next) + happiness(next, last)
            bestHappiness(next, others - next, newHappiness)
        }
    }
    return bestHappiness(first, others, 0)
}

private fun part1(input: List<String>): Int {
    val happiness = input.associate(::parse)
    val people = happiness.keys.map { it.first }.toSet()
    return calc({ a, b -> happiness[a to b]!! }, people.first(), people - people.first())
}

private fun part2(input: List<String>): Int {
    val happiness = input.associate(::parse)
    val people = happiness.keys.map { it.first }.toSet()
    return calc({ a, b -> if (a == "You" || b == "You") 0 else happiness[a to b]!! }, "You", people)
}

fun main() {
    val sample = """
        Alice would gain 54 happiness units by sitting next to Bob.
        Alice would lose 79 happiness units by sitting next to Carol.
        Alice would lose 2 happiness units by sitting next to David.
        Bob would gain 83 happiness units by sitting next to Alice.
        Bob would lose 7 happiness units by sitting next to Carol.
        Bob would lose 63 happiness units by sitting next to David.
        Carol would lose 62 happiness units by sitting next to Alice.
        Carol would gain 60 happiness units by sitting next to Bob.
        Carol would gain 55 happiness units by sitting next to David.
        David would gain 46 happiness units by sitting next to Alice.
        David would lose 7 happiness units by sitting next to Bob.
        David would gain 41 happiness units by sitting next to Carol.
    """.trimIndent().lines()
    check(part1(sample) == 330)

    val input = File("in/y2015/13.txt").readLines()
    println(part1(input))
    println(part2(input))
}
