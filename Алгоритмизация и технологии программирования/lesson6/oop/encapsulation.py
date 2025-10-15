class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance
        self._balance = balance

    def income(self, summ):
        self.__balance += summ

    def print_bal(self):
        print(self.__balance)


MyAcc = BankAccount('matvey')
MyAcc.income(1)
MyAcc.print_bal()
# сделать длину MClass приватной