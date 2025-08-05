package y2015

import java.io.File

private data class Reindeer(val name: String, val speed: Int, val flyTime: Int, val restTime: Int) {
    var points = 0
    fun distance(time: Int): Int {
        val cycleTime = flyTime + restTime
        return (time / cycleTime * flyTime + minOf(flyTime, time % cycleTime)) * speed
    }
}

private fun parse(s: String): Reindeer {
    val (name, speed, flyTime, restTime) = Regex("""(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.""")
        .find(s)!!.destructured
    return Reindeer(name, speed.toInt(), flyTime.toInt(), restTime.toInt())
}

private fun part1(input: List<String>, time: Int): Int {
    return input.map(::parse).maxOf { it.distance(time) }
}

private fun part2(input: List<String>, time: Int): Int {
    val reindeers = input.map(::parse)
    repeat(time) { currentTime ->
        val maxDistance = reindeers.maxOf { it.distance(currentTime + 1) }
        reindeers.filter { it.distance(currentTime + 1) == maxDistance }.forEach { it.points++ }
    }
    return reindeers.maxOf { it.points }
}

fun main() {
    val sample = """
        Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
        Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
    """.trimIndent().lines()
    check(part1(sample, 1000) == 1120)
    check(part2(sample, 1000) == 689)

    val input = File("in/y2015/14.txt").readLines()
    println(part1(input, 2503))
    println(part2(input, 2503))
}