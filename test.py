class MyClass:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def __add__(self, other):
        return MyClass(self.p1 + other.p1, self.p2 + other.p2, self.p3 + other.p3)
    def __str__(self):
        return f"P1: {self.p1} P2: {self.p2} P3 {self.p3}"


a = MyClass(1, 2, 3)
b = MyClass(4, 5, 6)
c = a + b + b + a + b + b
print(c)
