class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


NW = Vector(-1, -1)
NE = Vector(1, -1)
SW = Vector(-1, 1)
SE = Vector(1, 1)
N = Vector(0, -1)
S = Vector(0, 1)
W = Vector(-1, 0)
E = Vector(1, 0)

DIRS = (N, NE, E, SE, S, SW, W, NW)

TURN_RIGHT = {N: E, E: S, S: W, W: N}
TURN_LEFT = {N: W, W: S, S: E, E: N}

DIR_FROM_CHAR = {'^': N, 'v': S, '<': W, '>': E}
