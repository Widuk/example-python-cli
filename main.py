from src.entities.beverage import Beverage
from src.entities.ticket import Ticket
from src.entities.popcorn import Popcorn
from src.services.product_service import calculate_ticket_discount, sell_product
from src.utils.cli import ask_yes_or_no

print('Welcome!')
is_client = ask_yes_or_no('Are you a registered customer? (yes/no): ')
ticket_amount = sell_product(Ticket)
popcorn_amount = sell_product(Popcorn)
beverage_amount = sell_product(Beverage)
discount_amount = calculate_ticket_discount(ticket_amount, is_client)

print(f"""
Products:
    Tickets:          ${ticket_amount}
    Popcorns:         ${popcorn_amount}
    Beverages:        ${beverage_amount}
Discount:             ${discount_amount}
Total Amount:         ${round(sum([ticket_amount, popcorn_amount, beverage_amount, discount_amount]))}""")
