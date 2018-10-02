class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_on_curve(self):
        if self.y**2 -0.1 < (self.x**3 + 7) <= self.y**2+0.1:
            print("yes", self.x**3 + 7, self.y**2)
        else:
            print("NO", self.x**3 + 7, self.y**2)

    def add(self, other):
        s = (other.y - self.y)/(other.x - self.x)
        x3 = s**2 - self.x - other.x
        y3 = self.y + s*(x3 - self.x)
        print(x3, y3)


p1 = Point(-1.9, 0.37)
p1.is_on_curve()
p2 = Point(1, 2.82)
p1.add(p2)