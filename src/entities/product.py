class Product:
    """ Class to represent products for sale. The products have a menu option, and price. """
    def __init__(self, option: int, price: int) -> None:
        self.option = option
        self.price = price