from models.clothing import Clothing

class Wardrobe:
    def __init__(self):
        self.items = []

    def add_item(self, item: Clothing):
        self.items.append(item)
        return(f"{item.name} added!")

    def remove_item(self, item: Clothing):
        if item in self.items:
            self.items.remove(item)
            return(f"{item.name} deleted!")
        else:
            return(f"{item.name} not found!")

    def show_all_items(self):
        if not self.items:
            return("Wardrobe is empty!")
        for item in self.items:
            return(item)

    def filter_by_category(self, category):
        return [item for item in self.items if item.category == category]