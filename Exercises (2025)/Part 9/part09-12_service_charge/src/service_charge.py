"""sumary_line
Please create a class named BankAccount which models a bank account. The class should contain

a constructor which takes the name of the owner (str), account number (str) and balance (float) as arguments
a method deposit(amount: float) for depositing money to the account
a method withdraw(amount: float) for withdrawing money from the account
a getter method balance which returns the balance of the account
The class should also contain the private method

__service_charge(), which decreases the balance on the account by one percent. Whenever either of the methods deposit or withdraw is called, this method should also be called. The service charge is calculated and subtracted only after the actual operation is completed (that is, after the amount specified has been added to or subtracted from the balance).
All data attributes within the class definition should be private.

You may use the following code for testing your class:

account = BankAccount("Randy Riches", "12345-6789", 1000)
account.withdraw(100)
print(account.balance)
account.deposit(100)
print(account.balance)

Sample output
891.0
981.09
"""


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


"""
# Suggested solution
class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: float):
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance

    def __service_charge(self):
        self.__balance *= 0.99

    def deposit(self, amount: float):
        self.__balance += amount
        self.__service_charge()

    def withdraw(self, amount: float):
        self.__balance -= amount
        self.__service_charge()

    @property
    def balance(self):
        return self.__balance

#Review
My solution results in the same output, suggested one uses
the __service_charge classmethod without argument, which makes sense. 
It doesn,t however check if the amount to withdraw is not higher than what's 
on the balance!
"""
