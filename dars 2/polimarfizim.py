from math import pi

class Shape:
    def __init__(self, name) -> None:
        self.name = name

    def yuzi(self):
        pass

class Doira(Shape):
    def __init__(self, radius) -> None:
        super().__init__("Doira")
        self.radius = radius

    def yuzi(self):
        return self.radius**2*pi
    
    def __str__(self) -> str:
        return f"Doira yuzi: {self.yuzi()} ga teng."
    
obj = Doira(4)
print(obj)