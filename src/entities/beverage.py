from enum import Enum
from src.entities.product import Product

class Beverage(Enum):
    """ Class to represent the Beverage categories. Catalogue. Stores beverage products their menu option number and price. """
    SMALL = Product(1, 2000)
    MEDIUM = Product(2, 2250)
    LARGE = Product(3, 3000)