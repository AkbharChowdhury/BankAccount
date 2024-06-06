from atm_options import ATM
from bank_account import BankAccount, Helper


def border(name):
    def repeat(string, n):
        return string * n
    n = 20
    if not name:
        return repeat('*', n * 3)
    return repeat('*', n) + name.title().center(n) + repeat('*', n)


def display_menu():
    sep = ')'
    print(border("select an option"))
    for option in ATM:
        current_option = option.name.lower()
        if "_" in current_option:
            print(f'{option.value}{sep} {" ".join(current_option.split("_")).title()}')
            continue
        print(f'{option.value}{sep} {current_option.title()}')
    print(border(''))


def main():
    account = BankAccount(name="john", balance=1_500)
    while True:
        display_menu()
        choice = ATM(int(input("select an option: ".title())))
        match choice:
            case ATM.SHOW_BALANCE:
                print(account.show_balance())
            case ATM.DEPOSIT:
                amount = float(input('enter amount to deposit '.capitalize()))
                account.deposit(amount)
            case ATM.WITHDRAW:
                amount = float(input('Enter amount to withdraw '.capitalize()))
                if account.withdraw(amount):
                    print(f'{Helper.format_currency(amount)} was successfully withdrawn. ')
                    print(f'remaining balance {account.show_balance()}')
            case ATM.EXIT:
                print(f'thank you for banking with {BankAccount.name()}'.title())
                break


if __name__ == '__main__':
    main()
