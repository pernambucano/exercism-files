class BankAccount:
    def __init__(self):
        self.balance = 0
        self.is_open = False

    def get_balance(self):
        if self.is_open == False:
            raise ValueError("Can not get the current balance of a closed account.")
        return self.balance

    def open(self):
        if self.is_open == True:
            raise ValueError("Can not open an already opened account.")
        self.is_open = True
        self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Can not deposit negative values.")
        elif self.is_open == False:
            raise ValueError("Can not deposit into closed accounts.")

        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Can not withdraw more than the current balance.")
        elif amount < 0:
            raise ValueError("Can not withdraw negative numbers.")

        self.balance -= amount

    def close(self):
        if self.is_open == False:
            raise ValueError("Can not close an already closed account.")
        self.is_open = False
