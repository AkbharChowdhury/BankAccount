import babel.numbers as babel
from decimal import Decimal

import babel.numbers as babel
from decimal import Decimal
from colorama import init as colorama_init
from colorama import Style

colorama_init()


def text_colour(color, text):
    print(f'{color}{text}{Style.RESET_ALL}')


class Helper:

    @staticmethod
    def format_currency(amount):
        return babel.format_currency(Decimal(str(amount)), "GBP")
