from enum import Enum
from src.entities.product import Product

class Ticket(Enum):
    """ Class to represent the input categories. Catalogue. Stores input products with their menu option number and price. """
    PREMIERE = Product(1, 5800)
    NORMAL = Product(2, 3900)