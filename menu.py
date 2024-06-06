from atm_options import ATM


class Menu:

    def __border(self, name):
        def repeat(string, n):
            return string * n

        n = 20
        if not name:
            return repeat('*', n * 3)
        return repeat('*', n) + name.title().center(n) + repeat('*', n)

    def display_menu(self):
        sep = ')'
        print(self.__border("select an option"))
        for option in ATM:

            current_option = option.name.lower()
            if "_" in current_option:
                print(f'{option.value}{sep} {" ".join(current_option.split("_")).title()}')
                continue
            print(f'{option.value}{sep} {current_option.title()}')
        print(self.__border(''))
