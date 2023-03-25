from enum import Enum

from src.utils.cli import ask_yes_or_no

def select_product(product_catalog: Enum) -> Enum:
    """ Function to offer the selection of a product from a product catalog.
    - Any console entry that is not a number, or is outside the range of catalog options,
    prompts the user to respond again.

    Parameters:
    product_catalog (Enum): set of products from a catalog to be offered on the screen.

    Returns:
    product (Enum): product selected by the user.
    """
    while True:
        try:
            option = int(input(f'Select an option (1-{len(product_catalog)}): '))
            return next(product for product in product_catalog if product.value.option == option)
        except ( ValueError, StopIteration ):
            print("Please enter a valid value")

def ask_product_quantity(product_name: str) -> int:
    """ Function to consult the quantity of products to buy.
    - Any console entry that is not a number prompts the user to respond again.

    Parameters:
    product_name (str): name of the product to be displayed in the query.

    Returns:
    quantity (int): quantity of the product to buy.
    """
    while True:
        try:
            quantity = int(input(f'How many {product_name}s do you want?: '))
            if quantity <= 0: raise ValueError
            else: return quantity
        except ValueError:
            print("Please enter a valid value")

def sell_product(product_catalog: Enum) -> int:
    """ Function to make the sale of a product by console.

    Parameters:
    product_catalog (Enum): type of product to be sold by console.

    Returns:
    sale_amount (int): sale amount. It is equal to the price multiplied by the quantity of the product sold.
    """
    if ask_yes_or_no(f'Do you want to add {str(product_catalog.__name__).lower()}s to your order? (yes/no): '):
        print(f'What {str(product_catalog.__name__).lower()} do you want?')
        for option, product in enumerate(product_catalog, start=1):
            print(f'{product.value.option}. {product.name.capitalize()} → ${product.value.price}')
        return select_product(product_catalog).value.price * ask_product_quantity(product_catalog.__name__)
    else: return 0

def calculate_ticket_discount(ticket_amount: int, is_client: bool):
    if is_client:
        return round(-ticket_amount * 0.3)
    else:
        return 0
