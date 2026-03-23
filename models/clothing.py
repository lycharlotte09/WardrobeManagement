class Clothing:
    def __init__(self, name, category, color):
        self.name = name
        self.category = category
        self.color = color

    def __str__(self):
        return f"{self.name} ({self.category}, {self.color})"
    

class Top(Clothing):
    def __init__(self, name, color, sleeve_length):
        super().__init__(name, "Top", color)
        self.sleeve_length = sleeve_length

class Bottom(Clothing):
    def __init__(self, name, color, style):
        super().__init__(name, "Bottom", color)
        self.style = style

class Shoes(Clothing):
    def __init__(self, name, color, shoe_type):
        super().__init__(name, "Shoes", color)
        self.shoe_type = shoe_type
    