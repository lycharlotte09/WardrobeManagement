from models.clothing import Clothing

class Wardrobe:
    def __init__(self):
        self.items = []

    def add_item(self, item: Clothing):
        self.items.append(item)
        print(f"{item.name} added!")

    def remove_item(self, item: Clothing):
        if item in self.items:
            self.items.remove(item)
            print(f"{item.name} deleted!")
        else:
            print(f"{item.name} not found!")

    def show_all_items(self):
        if not self.items:
            print("Wardrobe is empty!")
        for item in self.items:
            print(item)

    def filter_by_category(self, category):
        return [item for item in self.items if item.category == category]