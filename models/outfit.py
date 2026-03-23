from random import choice

class Outfit:
    def __init__(self, top=None, bottom=None, shoes=None):
        self.top = top
        self.bottom = bottom
        self.shoes = shoes

    def __str__(self):
        return f"Outfit:\nTop: {self.top}\nBottom: {self.bottom}\nShoes: {self.shoes}"

    @staticmethod
    def generate_random(wardrobe):
        tops = wardrobe.filter_by_category("Top")
        bottoms = wardrobe.filter_by_category("Bottom")
        shoes = wardrobe.filter_by_category("Shoes")
        
        if not tops or not bottoms or not shoes:
            print("Not enough clothes in the wardrobe!")
            return None
        
        return Outfit(
            top=choice(tops),
            bottom=choice(bottoms),
            shoes=choice(shoes)
        )