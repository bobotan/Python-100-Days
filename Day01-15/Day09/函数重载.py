class Vector:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    def __str__(self):
        return "Vector (%d, %d)" % (self._a, self._b)

    def __add__(self, other):
        return Vector(self._a + other.a, self._b + other.b)


v1 = Vector(1, 2)
v2 = Vector(3, -5)
print(v1 + v2)
