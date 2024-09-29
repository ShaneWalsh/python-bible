


class Account:
    def __init__(self,name,balance,min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def desposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("No funds")

    def statement(self):
        details = [self.name, self.balance, self.min_balance]
        print("Account {} has {} with a minimum of {}".format(*details))

class CurrentAccount(Account):
    def __init__(self, name, balance):
        super().__init__(name,balance,min_balance = -1000)

acc = CurrentAccount("Shanes AC", 500)

acc.statement()
acc.desposit(500)
acc.statement()
acc.withdraw(2000)
acc.statement()
acc.withdraw(1)
acc.statement()
