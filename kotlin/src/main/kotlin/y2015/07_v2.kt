package y2015

import java.io.File

private class Gate2(val left: String, val right: String, val op: (Int, Int) -> Int)

private fun calcSignal(gates: Map<String, Gate2>, s: String, override: Pair<String, Int>? = null): Int {
    val signalValues = override?.let { mutableMapOf(it) } ?: mutableMapOf()

    fun eval(s: String): Int {
        var result = s.toIntOrNull() ?: signalValues[s]
        if (result == null) {
            result = gates[s]!!.let { gate -> gate.op(eval(gate.left), eval(gate.right)) }
            signalValues[s] = result
        }
        return result
    }

    return eval(s)
}

private fun parse(input: List<String>) = input
    .map(Regex("""^(\w*?)( AND | OR | LSHIFT | RSHIFT |NOT |)(\w+) -> (\w+)$""")::find)
    .map { it!!.destructured }
    .associate { (left, op, right, result) ->
        result to when (op.trim()) {
            "" -> Gate2(right, "0", Int::xor)
            "NOT" -> Gate2(right, "65535", Int::xor)
            "AND" -> Gate2(left, right, Int::and)
            "OR" -> Gate2(left, right, Int::or)
            "LSHIFT" -> Gate2(left, right, Int::shl)
            "RSHIFT" -> Gate2(left, right, Int::ushr)
            else -> throw IllegalArgumentException()
        }
    }

fun main() {
    val sample = parse(
        """
        123 -> x
        456 -> y
        x AND y -> d
        x OR y -> e
        x LSHIFT 2 -> f
        y RSHIFT 2 -> g
        NOT x -> h
        NOT y -> i
    """.trimIndent().lines()
    )
    check(calcSignal(sample, "d") == 72)
    check(calcSignal(sample, "e") == 507)
    check(calcSignal(sample, "f") == 492)
    check(calcSignal(sample, "g") == 114)
    check(calcSignal(sample, "h") == 65412)
    check(calcSignal(sample, "i") == 65079)
    check(calcSignal(sample, "x") == 123)
    check(calcSignal(sample, "y") == 456)

    val gates = parse(File("in/y2015/07.txt").readLines())
    val a = calcSignal(gates, "a")
    println(a)
    println(calcSignal(gates, "a", "b" to a))
}
