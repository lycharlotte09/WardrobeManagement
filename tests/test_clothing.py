import unittest
from models.clothing import Clothing, Top, Bottom, Shoes


class TestClothing(unittest.TestCase):

    def test_clothing_creation(self):
        item = Clothing("T-Shirt", "Top", "red")

        self.assertEqual(item.name, "T-Shirt")
        self.assertEqual(item.category, "Top")
        self.assertEqual(item.color, "red")
        self.assertIsNone(item.image_path)

    def test_clothing_str(self):
        item = Clothing("T-Shirt", "Top", "red")
        self.assertEqual(str(item), "T-Shirt (Top, red)")


class TestTop(unittest.TestCase):

    def test_top_creation(self):
        top = Top("Hoodie", "black", "long")

        self.assertEqual(top.name, "Hoodie")
        self.assertEqual(top.category, "Top")
        self.assertEqual(top.color, "black")
        self.assertEqual(top.sleeve_length, "long")


class TestBottom(unittest.TestCase):

    def test_bottom_creation(self):
        bottom = Bottom("Jeans", "blue", "skinny")

        self.assertEqual(bottom.name, "Jeans")
        self.assertEqual(bottom.category, "Bottom")
        self.assertEqual(bottom.color, "blue")
        self.assertEqual(bottom.style, "skinny")


class TestShoes(unittest.TestCase):

    def test_shoes_creation(self):
        shoes = Shoes("Nike", "white", "sneaker")

        self.assertEqual(shoes.name, "Nike")
        self.assertEqual(shoes.category, "Shoes")
        self.assertEqual(shoes.color, "white")
        self.assertEqual(shoes.shoe_type, "sneaker")


if __name__ == "__main__":
    unittest.main()