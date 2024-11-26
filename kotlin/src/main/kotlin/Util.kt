data class Vec2(val x: Int, val y: Int) {
    operator fun plus(other: Vec2) = Vec2(x + other.x, y + other.y)
    operator fun plus(dir: Dir) = Vec2(x + dir.dx, y + dir.dy)

    companion object {
        val ZERO = Vec2(0, 0)
    }
}

enum class Dir(val dx: Int, val dy: Int) {
    O(0, 0),
    N(0, -1), E(1, 0), S(0, 1), W(-1, 0),
    NE(1, -1), SE(1, 1), SW(-1, 1), NW(-1, -1);

    operator fun component1() = dx
    operator fun component2() = dy

    companion object {
        val ALL = entries
        val NEIGHBORS = listOf(N, E, S, W, NE, SE, SW, NW)
        val CARDINAL = listOf(N, E, S, W)
        val DIAGONAL = listOf(NE, SE, SW, NW)
        fun neighborsOf(x: Int, y: Int) = NEIGHBORS.map { Vec2(x + it.dx, y + it.dy) }
        fun neighborsOf(pos: Vec2) = neighborsOf(pos.x, pos.y)

        fun fromArrowChar(c: Char): Dir = when (c) {
            '^' -> N
            'v' -> S
            '<' -> W
            '>' -> E
            else -> throw IllegalArgumentException()
        }

    }
}

data class Rect(val x0: Int, val y0: Int, val w: Int, val h: Int) {
    val topLeft = Vec2(x0, y0)
    val topRight = Vec2(x0 + w - 1, y0)
    val bottomLeft = Vec2(x0, y0 + h - 1)
    val bottomRight = Vec2(x0 + w - 1, y0 + h - 1)

    fun points() = (0..<h).asSequence().flatMap { y -> (0..<w).asSequence().map { x -> Vec2(x0 + x, y0 + y) } }
    fun corners() = sequenceOf(topLeft, topRight, bottomLeft, bottomRight)

    companion object {
        fun ofSize(width: Int, height: Int) = Rect(0, 0, width, height)
        fun fromCorners(topLeftX: Int, topLeftY: Int, bottomRightX: Int, bottomRightY: Int) =
            Rect(topLeftX, topLeftY, bottomRightX - topLeftX + 1, bottomRightY - topLeftY + 1)
    }
}

fun <T> permutations(data: Set<T>): Sequence<List<T>> = sequence {
    fun helper(src: Set<T>, result: List<T>): Sequence<List<T>> = sequence {
        if (src.isEmpty()) {
            yield(result)
        } else {
            for (e in src) {
                yieldAll(helper(src - e, result + e))
            }
        }
    }
    yieldAll(helper(data, emptyList()))
}
