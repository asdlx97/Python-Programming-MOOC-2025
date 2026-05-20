# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, owner: str, acc_nr: str, balance: float):
        self.__owner = owner
        self.__aid = acc_nr
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount: float):
        self.__balance += amount
        self.__balance = self.__service_charge(self.__balance)

    def withdraw(self, amount: float):
        if self.__balance >= amount:
            self.__balance -= amount
            self.__balance = self.__service_charge(self.__balance)

    def __service_charge(self, balance):
        return balance * 0.99


if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)
