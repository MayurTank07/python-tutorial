class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder      # Public
        self.__balance = balance                  # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn.")
        else:
            print("Insufficient balance.")

    def getBalance(self):
        return self.__balance

acc = BankAccount("Dexter", 80000)
print("\n\n Initial Acc Holder and Balance Value")
print("acc holder : ", acc.account_holder)
print("acc bal : ", acc.getBalance())

print("\n\n After Deposit Acc Holder and Balance Value")
acc.deposit(10000)
print("acc bal : ", acc.getBalance())

print("\n\n After Withdrawal Acc Holder and Balance Value")
acc.withdraw(20000)
print("acc bal : ", acc.getBalance())