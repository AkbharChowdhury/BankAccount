from colorama import Fore
from atm_options import ATM
from bank_account import BankAccount
from menu import Menu
from helper import Helper, text_colour


def main():
    account = BankAccount(name="john", balance=1_500)
    menu = Menu()
    while True:
        menu.display_menu()
        choice = ATM(int(input("select an option: ".title())))
        match choice:
            case ATM.SHOW_BALANCE:
                account.show_balance()
            case ATM.DEPOSIT:
                amount = float(input('enter amount to deposit '.capitalize()))
                account.deposit(amount)
            case ATM.WITHDRAW:
                amount = float(input('Enter amount to withdraw '.capitalize()))
                if account.withdraw(amount):
                    f'{text_colour(Fore.GREEN, f"{Helper.format_currency(amount)} was successfully withdrawn.")}'
                    print(f'remaining balance:'.title())
                    account.show_balance()
            case ATM.EXIT:
                print(f'thank you for banking with {BankAccount.name()}'.title())
                break


if __name__ == '__main__':
    main()
