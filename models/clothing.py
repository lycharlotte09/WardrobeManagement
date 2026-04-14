class Clothing:
    def __init__(self, name, category, color, image_path = None):
        self.name = name
        self.category = category
        self.color = color
        self.image_path = image_path

    def __str__(self):
        return f"{self.name} ({self.category}, {self.color})"
    

class Top(Clothing):
    def __init__(self, name, color, sleeve_length, image_path=None):
        super().__init__(name, "Top", color, image_path)
        self.sleeve_length = sleeve_length

class Bottom(Clothing):
    def __init__(self, name, color, style, image_path = None):
        super().__init__(name, "Bottom", color, image_path)
        self.style = style

class Shoes(Clothing):
    def __init__(self, name, color, shoe_type, image_path=None):
        super().__init__(name, "Shoes", color, image_path)
        self.shoe_type = shoe_type
    