import babel.numbers as babel
from decimal import Decimal
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()


class Helper:
    @staticmethod
    def format_currency(amount):
        return babel.format_currency(Decimal(str(amount)), "GBP")


def text_colour(color, text):
    print(f'{color}{text}{Style.RESET_ALL}')


class BankAccount:
    __DEFAULT_COLOUR = Fore.GREEN

    @staticmethod
    def name():
        return "Halifax"

    def __init__(self, name: str, balance: float):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        text_colour(BankAccount.__DEFAULT_COLOUR,
                    f'Deposit {self.name.title()} with {Helper.format_currency(amount)} Balance')

    def withdraw(self, amount):
        if amount > self.__balance:
            text_colour(color=Fore.RED, text=f'Amount {Helper.format_currency(amount)} is greater than balance!')
            return False
        self.__balance -= amount
        return True

    def show_balance(self):
        return Helper.format_currency(self.__balance)

    def __str__(self):
        return f'{self.name}: {self.__balance}'
