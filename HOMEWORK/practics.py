from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self, loan):
        self.balance = loan

    @abstractmethod
    def deposit_loan(self, amount):
        pass

    @abstractmethod
    def withdraw_loan(self, amount):
        pass


class Saving(Account):

    def deposit_loan(self, amount):
        self.balance -= amount

        if self.balance <= 0:
            print("Loan fully paid")
            self.balance = 0

    def withdraw_loan(self, amount):
        self.balance += amount


s = Saving(10000)

print("Loan:", s.balance)

s.deposit_loan(5000)
print("Remaining Loan:", s.balance)

s.deposit_loan(5000)
print("Remaining Loan:", s.balance)