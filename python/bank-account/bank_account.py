import threading


class BankAccount:
    def __init__(self):
        self.balance = 0
        self.is_open = False
        self.lock = threading.Lock()

    def validate_if_open(self):
        if self.is_open == False:
            raise ValueError("Account not opened.")

    def get_balance(self):
        with self.lock:
            self.validate_if_open()
            return self.balance

    def open(self):
        with self.lock:
            if self.is_open == True:
                raise ValueError("Already opened.")
            self.is_open = True
            self.balance = 0

    def deposit(self, amount):
        with self.lock:
            if amount < 0:
                raise ValueError("Can not deposit negative values.")
            self.validate_if_open()
            self.balance += amount

    def withdraw(self, amount):
        with self.lock:
            self.validate_if_open()
            if amount > self.balance:
                raise ValueError("Can not withdraw more than the current balance.")
            elif amount < 0:
                raise ValueError("Can not withdraw negative numbers.")
            self.balance -= amount

    def close(self):
        with self.lock:
            if self.is_open == False:
                raise ValueError("Account already closed.")
            self.is_open = False
