import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self):
        ab = self.a.distance(self.b)
        bc = self.b.distance(self.c)
        ca = self.c.distance(self.a)
        return ab + bc > ca and bc + ca > ab and ca + ab > bc

    def area(self):
        if not self.is_valid():
            return "INVALID"
        ab = self.a.distance(self.b)
        bc = self.b.distance(self.c)
        ca = self.c.distance(self.a)
        s = (ab + bc + ca) / 2
        return round(math.sqrt(s * (s - ab) * (s - bc) * (s - ca)), 2)


t = int(input())
for i in range(t):
    x1, y1, x2, y2, x3, y3 = map(float, input().split())
    a = Point(x1, y1)
    b = Point(x2, y2)
    c = Point(x3, y3)
    triangle = Triangle(a, b, c)
    print(triangle.area())
