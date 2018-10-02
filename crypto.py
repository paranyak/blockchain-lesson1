class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_on_curve(self):
        if self.y**2 -0.1< (self.x**3 + 7) <= self.y**2+0.1:
            print("yes", self.x**3 + 7, self.y**2)
        else:
            print("NO", self.x**3 + 7, self.y**2)

p1 = Point(1, 2.82)
p1.is_on_curve()