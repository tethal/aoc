package y2015

import java.io.File

private sealed interface Gate {
    data class Copy(val input: String) : Gate
    data class Not(val input: String) : Gate
    data class And(val left: String, val right: String) : Gate
    data class Or(val left: String, val right: String) : Gate
    data class LShift(val left: String, val right: String) : Gate
    data class RShift(val left: String, val right: String) : Gate
}

private fun calcSignal(gates: Map<String, Gate>, s: String, override: Pair<String, Int>? = null): Int {
    val signalValues = mutableMapOf<String, Int>()
    override?.let { (name, value) -> signalValues[name] = value }

    fun eval(s: String): Int {
        signalValues[s]?.let { return it }
        s.toIntOrNull()?.let { return it }
        val value = when (val gate = gates[s]!!) {
            is Gate.Copy -> eval(gate.input)
            is Gate.Not -> eval(gate.input) xor 0xffff
            is Gate.And -> eval(gate.left) and eval(gate.right)
            is Gate.Or -> eval(gate.left) or eval(gate.right)
            is Gate.LShift -> eval(gate.left) shl eval(gate.right)
            is Gate.RShift -> eval(gate.left) ushr eval(gate.right)
        }
        signalValues[s] = value
        return value
    }

    return eval(s)
}

private fun parse(input: List<String>) = input.associate { line ->
    val (lhs, resultName) = line.split(" -> ")
    val gate = when {
        lhs.contains("AND") -> {
            val (a, b) = lhs.split(" AND ")
            Gate.And(a, b)
        }

        lhs.contains("OR") -> {
            val (a, b) = lhs.split(" OR ")
            Gate.Or(a, b)
        }

        lhs.contains("LSHIFT") -> {
            val (a, b) = lhs.split(" LSHIFT ")
            Gate.LShift(a, b)
        }

        lhs.contains("RSHIFT") -> {
            val (a, b) = lhs.split(" RSHIFT ")
            Gate.RShift(a, b)
        }

        lhs.contains("NOT") -> Gate.Not(lhs.split("NOT ")[1])

        else -> Gate.Copy(lhs)
    }
    resultName to gate
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
