from enum import Enum
from src.entities.product import Product

class Popcorn(Enum):
    """ Class to represent the categories of popcorn. Catalogue. Stores popcorn products with their menu option number and price. """
    SMALL = Product(1, 3500)
    MEDIUM = Product(2, 4500)
    LARGE = Product(3, 8800)