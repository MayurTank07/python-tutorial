class ATM:
    def __init__(self, pin):
        self.__pin = pin     # Private
        self.__balance = 0   # Private

    def authenticate(self, entered_pin):
        return entered_pin == self.__pin

    def deposit(self, pin, amount):
        if self.authenticate(pin):
            self.__balance += amount
            print("Amount deposited.")
        else:
            print("Authentication failed!")

    def check_balance(self, pin):
        if self.authenticate(pin):
            return self.__balance
        else:
            return "Access Denied"

# Test
atm = ATM("1234")
atm.deposit("1234", 5000)
print("Balance:", atm.check_balance("1234"))
print("Balance (wrong pin):", atm.check_balance("0000"))
