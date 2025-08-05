package y2015

import java.io.File

private sealed interface Opcode
private data class Hlf(val reg: Int) : Opcode
private data class Tpl(val reg: Int) : Opcode
private data class Inc(val reg: Int) : Opcode
private data class Jmp(val offset: Int) : Opcode
private data class Jie(val reg: Int, val offset: Int) : Opcode
private data class Jio(val reg: Int, val offset: Int) : Opcode

private fun parse(src: String): Opcode {
    return when (src.substring(0, 3)) {
        "hlf" -> Hlf(src[4] - 'a')
        "tpl" -> Tpl(src[4] - 'a')
        "inc" -> Inc(src[4] - 'a')
        "jmp" -> Jmp(src.substring(4).toInt())
        "jie" -> Jie(src[4] - 'a', src.substring(7).toInt())
        "jio" -> Jio(src[4] - 'a', src.substring(7).toInt())
        else -> throw IllegalArgumentException()
    }
}

private fun execute(code: List<Opcode>, aInit: Int): Int {
    var pc = 0
    val registers = intArrayOf(aInit, 0)
    while (pc < code.size) {
        when (val instr = code[pc]) {
            is Hlf -> registers[instr.reg] /= 2
            is Tpl -> registers[instr.reg] *= 3
            is Inc -> registers[instr.reg]++
            is Jmp -> pc += instr.offset - 1
            is Jie -> if (registers[instr.reg] % 2 == 0) pc += instr.offset - 1
            is Jio -> if (registers[instr.reg] == 1) pc += instr.offset - 1
        }
        pc++
    }
    return registers[1]
}

fun main() {
    val input = File("in/y2015/23.txt").readLines()
    val code = input.map(::parse)
    println(execute(code, 0))
    println(execute(code, 1))
}
