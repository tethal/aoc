package y2015

import java.io.File

private enum class UnaryOperator {
    NOT, COPY
}

private enum class BinaryOperator {
    AND, OR, RSHIFT, LSHIFT
}

private fun calc(signalName: String, signals: Map<String, Signal>, foundSignals: MutableMap<String, Int>): Int {
    if (signalName.toIntOrNull() != null) {
        return signalName.toInt()
    }
    if (foundSignals.containsKey(signalName)) {
        return foundSignals[signalName]!!
    }
    val result = signals[signalName]!!.calculate(signals, foundSignals)
    foundSignals[signalName] = result
    return result
}

private fun doFirst(lines: List<String>): Int {
    val signals = lines.map { getOneOfTheSignal(it) }.associate {
        when (it) {
            is BinarySignal -> it.result to it
            is UnarySignal -> it.result to it
        }
    }
    return calc("a", signals, mutableMapOf())
}

private sealed class Signal {
    abstract fun calculate(signals: Map<String, Signal>, foundSignals: MutableMap<String, Int>): Int
}

private data class BinarySignal(
    val valueA: String,
    val operator: BinaryOperator,
    val valueB: String,
    val result: String
) :
    Signal() {
    override fun calculate(signals: Map<String, Signal>, foundSignals: MutableMap<String, Int>): Int {
        val valueA = calc(this.valueA, signals, foundSignals)
        val valueB = calc(this.valueB, signals, foundSignals)

        return when (this.operator) {
            BinaryOperator.AND -> valueA and valueB
            BinaryOperator.OR -> valueA or valueB
            BinaryOperator.LSHIFT -> valueA shl valueB
            BinaryOperator.RSHIFT -> valueA shr valueB
        }
    }
}

private data class UnarySignal(val operator: UnaryOperator, val value: String, val result: String) : Signal() {
    override fun calculate(signals: Map<String, Signal>, foundSignals: MutableMap<String, Int>): Int {
        val value = calc(this.value, signals, foundSignals)
        return when (operator) {
            UnaryOperator.COPY -> value
            UnaryOperator.NOT -> 65536 + value.inv()
        }
    }
}

private fun getOneOfTheSignal(line: String): Signal {
    val regex1 = "^(\\w{1,3}) (AND|OR|RSHIFT|LSHIFT) (\\w{1,3}) -> (\\w{1,3})".toRegex()
    val regex2 = "^(NOT )?(\\w{1,5}) -> (\\w{1,3})".toRegex()

    fun getBinarySignal(matchResult: MatchResult): BinarySignal? {
        val (a, operator, b, result) = matchResult.destructured
        val eOperator = when (operator) {
            "AND" -> BinaryOperator.AND
            "OR" -> BinaryOperator.OR
            "LSHIFT" -> BinaryOperator.LSHIFT
            "RSHIFT" -> BinaryOperator.RSHIFT
            else -> throw IllegalArgumentException("Unknown operator")
        }
        return BinarySignal(a, eOperator, b, result)
    }

    fun getUnarySignal(matchResult: MatchResult): UnarySignal? {
        val (operator, a, result) = matchResult.destructured
        val eOperator = when (operator.trim()) {
            "NOT" -> UnaryOperator.NOT
            else -> UnaryOperator.COPY
        }
        return UnarySignal(eOperator, a, result)
    }

    var signal: Signal? = getSignal(regex1, line, ::getBinarySignal)
    signal = signal ?: getSignal(regex2, line, ::getUnarySignal)

    return signal!!
}

private fun <T : Signal> getSignal(regex: Regex, line: String, get: (MatchResult) -> T?): T? {
    val matchResult = regex.find(line)

    return if (matchResult != null) {
        get(matchResult)
    } else {
        null
    }
}


fun main() {
    print(doFirst(File("in/y2015/07.txt").readLines().toMutableList()))
}