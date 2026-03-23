from models.clothing import Clothing, Top, Bottom, Shoes
from models.wardrobe import Wardrobe
from models.outfit import Outfit

my_wardrobe = Wardrobe()

my_wardrobe.add_item(Top("sexy Red", "red", "short"))
my_wardrobe.add_item(Bottom("baggy grey", "grey", "Jeans"))
my_wardrobe.add_item(Shoes("adidas samba", "black", "Sneaker"))
my_wardrobe.add_item(Top("long Red", "red", "long"))
my_wardrobe.add_item(Bottom("skinny grey", "grey", "Jeans"))
my_wardrobe.add_item(Shoes("adidas samba", "green", "Sneaker"))

my_wardrobe.show_all_items()

outfit = Outfit.generate_random(my_wardrobe)
if outfit:
    print(outfit)