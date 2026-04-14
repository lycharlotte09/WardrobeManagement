from models.clothing import Clothing, Top, Bottom, Shoes
from models.wardrobe import Wardrobe
from models.outfit import Outfit

my_wardrobe = Wardrobe()



my_wardrobe.show_all_items()

outfit = Outfit.generate_random(my_wardrobe)
if outfit:
    print(outfit)