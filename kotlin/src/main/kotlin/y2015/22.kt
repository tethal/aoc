package y2015

import java.io.File
import kotlin.math.max

private enum class Spell(val cost: Int) {
    MAGIC_MISSILE(53), DRAIN(73), SHIELD(113), POISON(173), RECHARGE(229)
}

private data class GameState(
    val playerHp: Int,
    val playerMana: Int,
    val bossHp: Int,
    val bossDamage: Int,
    val shieldTurns: Int = 0,
    val poisonTurns: Int = 0,
    val rechargeTurns: Int = 0,
    val spentMana: Int = 0,
    val hardMode: Boolean = false,
) {

    fun newStateBuilder() = Builder(this)

    class Builder(oldState: GameState) {
        var playerHp = oldState.playerHp
        var playerMana = oldState.playerMana
        var bossHp = oldState.bossHp
        var bossDamage = oldState.bossDamage
        var shieldTurns = oldState.shieldTurns
        var poisonTurns = oldState.poisonTurns
        var rechargeTurns = oldState.rechargeTurns
        var spentMana = oldState.spentMana
        val hardMode = oldState.hardMode

        fun isSpellActive(spell: Spell) = when (spell) {
            Spell.SHIELD -> shieldTurns > 0
            Spell.POISON -> poisonTurns > 0
            Spell.RECHARGE -> rechargeTurns > 0
            else -> false
        }

        fun applyEffects() {
            if (shieldTurns > 0) {
                shieldTurns--
            }
            if (poisonTurns > 0) {
                bossHp -= 3
                poisonTurns--
            }
            if (rechargeTurns > 0) {
                playerMana += 101
                rechargeTurns--
            }
        }

        fun build() = GameState(
            playerHp, playerMana, bossHp, bossDamage, shieldTurns, poisonTurns, rechargeTurns, spentMana, hardMode
        )
    }
}

private fun doTurn(state: GameState, spell: Spell): Int {
    val newState = state.newStateBuilder()
    if (state.hardMode) {
        newState.playerHp--
        if (newState.playerHp <= 0) {
            return Int.MAX_VALUE
        }
    }
    newState.applyEffects()
    if (newState.bossHp <= 0) {
        return newState.spentMana
    }
    if (spell.cost > newState.playerMana || newState.isSpellActive(spell)) {
        return Int.MAX_VALUE
    }
    newState.playerMana -= spell.cost
    newState.spentMana += spell.cost
    when (spell) {
        Spell.MAGIC_MISSILE -> newState.bossHp -= 4
        Spell.DRAIN -> {
            newState.bossHp -= 2
            newState.playerHp += 2
        }

        Spell.SHIELD -> newState.shieldTurns = 6
        Spell.POISON -> newState.poisonTurns = 6
        Spell.RECHARGE -> newState.rechargeTurns = 5
    }
    if (newState.bossHp <= 0) {
        return newState.spentMana
    }
    newState.applyEffects()
    val playerArmor = if (newState.shieldTurns > 0) 7 else 0
    val damage = max(1, state.bossDamage - playerArmor)
    newState.playerHp -= damage
    if (newState.playerHp <= 0) {
        return Int.MAX_VALUE
    }
    val newStateBuilt = newState.build()
    return Spell.entries.minOfOrNull { nextSpell -> doTurn(newStateBuilt, nextSpell) }
        ?: Int.MAX_VALUE
}

private fun play(initialState: GameState): Int {
    return Spell.entries.minOfOrNull { spell -> doTurn(initialState, spell) } ?: Int.MAX_VALUE
}

fun main() {
    val input = File("in/y2015/22.txt").readLines()
    val (bossHp, bossDamage) = input.map { line -> line.split(": ")[1].toInt() }.let { it[0] to it[1] }
    println(play(GameState(50, 500, bossHp, bossDamage, hardMode = false)))
    println(play(GameState(50, 500, bossHp, bossDamage, hardMode = true)))
}
