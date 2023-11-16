# Basic Cash Register
# includes total price and number of items

import locale

locale.setlocale(locale.LC_ALL, 'en_US')

# cash register function for total and item counts
class CashRegister:
    def __init__(self):
        self.total = 0
        self.item_price = 0.0
        self.total_items = 0

    def add_items(self, price):
        self.item_price = price
        self.total = self.total + price
        print("Current total: ", locale.currency(self.item_price, symbol=True))
        self.total_items = self.total_items + 1
        print("Current item count: ", self.total_items)
        print("-"*50)

    def get_total(self):
        # return self.total
        return locale.currency(self.total, symbol=True)

    def get_count(self):
        return self.total_items

#user inputs
def main():
    register = CashRegister()
    print("Welcome to Generic Item Shop!")
    print("-"*50)
    while True:
        print("Please enter price of item or 'Q' to end: ")
        number = input(">>>> $")
        if number.strip().lower() == 'q':
            break
        try:
            num = float(number)
        except ValueError:
            print("Invalid number entered.")
            print("-"*50)
            continue
        else:
            register.add_items(num)
    print("The total price is: ", register.get_total())
    print("The total item count is: ", register.get_count())

# run program
if __name__ == "__main__":
    main()
