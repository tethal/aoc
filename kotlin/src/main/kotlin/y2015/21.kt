package y2015

import java.io.File

private data class Item(val name: String, val cost: Int, val damage: Int, val armor: Int)
private data class Character(val hp: Int, val damage: Int, val armor: Int)

private val weapons = listOf(
    Item("Dagger", 8, 4, 0),
    Item("Shortsword", 10, 5, 0),
    Item("Warhammer", 25, 6, 0),
    Item("Longsword", 40, 7, 0),
    Item("Greataxe", 74, 8, 0)
)

private val armors = listOf(
    Item("None", 0, 0, 0),
    Item("Leather", 13, 0, 1),
    Item("Chainmail", 31, 0, 2),
    Item("Splintmail", 53, 0, 3),
    Item("Bandedmail", 75, 0, 4),
    Item("Platemail", 102, 0, 5)
)

private val rings = listOf(
    Item("None", 0, 0, 0),
    Item("Damage +1", 25, 1, 0),
    Item("Damage +2", 50, 2, 0),
    Item("Damage +3", 100, 3, 0),
    Item("Defense +1", 20, 0, 1),
    Item("Defense +2", 40, 0, 2),
    Item("Defense +3", 80, 0, 3)
)

private fun equipCombos(): Sequence<Pair<Int, Character>> = sequence {
    for (weapon in weapons) {
        for (armor in armors) {
            for (ring1 in rings) {
                for (ring2 in rings) {
                    if (ring1 == ring2 && ring1 != rings[0]) continue
                    val cost = weapon.cost + armor.cost + ring1.cost + ring2.cost
                    val damage = weapon.damage + armor.damage + ring1.damage + ring2.damage
                    val armor = weapon.armor + armor.armor + ring1.armor + ring2.armor
                    yield(cost to Character(100, damage, armor))
                }
            }
        }
    }
}

private fun turnsToBeat(attacker: Character, defender: Character): Int {
    val dmgPerTurn = Math.max(1, attacker.damage - defender.armor)
    return (defender.hp + dmgPerTurn - 1) / dmgPerTurn
}

private fun Character.beats(boss: Character): Boolean {
    return turnsToBeat(this, boss) <= turnsToBeat(boss, this)
}

private fun part1(boss: Character) =
    equipCombos()
        .filter { (_, player) -> player.beats(boss) }
        .minOf { it.first }

private fun part2(boss: Character) =
    equipCombos()
        .filter { (_, player) -> !player.beats(boss) }
        .maxOf { it.first }

fun main() {
    check(turnsToBeat(Character(8, 5, 5), Character(12, 7, 2)) == 4)

    val input = File("in/y2015/21.txt").readLines()
    val boss = input.map { line -> line.split(": ")[1].toInt() }.let { Character(it[0], it[1], it[2]) }
    println(part1(boss))
    println(part2(boss))
}
