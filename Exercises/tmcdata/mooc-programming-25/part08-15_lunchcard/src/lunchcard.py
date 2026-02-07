"""sumary_line
NB: Some exercises have multiple parts, and
you can receive points for the different parts
separately. You can submit a partially completed
exercise by choosing 'Submit Solution' from the
menu next to the button for executing tests .

At Unicafe, the student cafeteria at the University
of Helsinki, students can pay for their lunch with
a special debit card.

In this exercise you will write a class called LunchCard,
with the purpose of emulating the functions provided by
the cafeteria's debit card.

The structure of the new class

Please create a new class named LunchCard.

First write the constructor for the class. It should
take the initial balance available on the card as an
argument, and save it as an attribute. This is provided
for you in the skeleton below.

Next, write a __str__ method, which returns a string
containing the balance: "The balance is X euros". The
available balance should be printed out with one decimal
place precision. Please see the example below for usage.

Here is a skeleton implementation for the class:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        pass
A usage example:

card = LunchCard(50)
print(card)
Executing the above should produce the following printout:

Sample output
The balance is 50.0 euros
Paying for lunch

Please implement the following methods in your LunchCard class:

eat_lunch subtracts 2.60 euros from the balance on the card
eat_special subtracts 4.60 euros from the balance on the card
You can use the following main function to test your class:

card = LunchCard(50)
print(card)

card.eat_lunch()
print(card)

card.eat_special()
card.eat_lunch()
print(card)
This should produce the following printout:

Sample output
The balance is 50.0 euros
The balance is 47.4 euros
The balance is 40.2 euros
Make sure the balance is never allowed to reach numbers
below zero:

card = LunchCard(4)
print(card)

card.eat_lunch()
print(card)

card.eat_lunch()
print(card)

Sample output
The balance is 4.0 euros
The balance is 1.4 euros
The balance is 1.4 euros
If there is not enough money on the card to pay for
the lunch, the price of the lunch should not be subtracted
from the balance.

Depositing money on the card

Implement the deposit_money method in your LunchCard class.

The method increases the balance on the card by the amount
given as an argument.

card = LunchCard(10)
print(card)
card.deposit_money(15)
print(card)
card.deposit_money(10)
print(card)
card.deposit_money(200)
print(card)

Sample output
The balance is 10.0 euros
The balance is 25.0 euros
The balance is 35.0 euros
The balance is 235.0 euros
The method should account for arguments below zero by raising an exception of type ValueError:

card = LunchCard(10)
card.deposit_money(-10)
Sample output
File "testi.py", line 3, in lunchcard
ValueError: You cannot deposit an amount of money less than zero
NB: this method should raise an exception. Please see the instructions for raising exceptions in part 6. Under no circumstances should the method itself print out anything - the example above is a printout from the Python interpreter coming across the exception.

Multiple cards

Please write a main function which contains the following sequence of events:

Create a lunch card for Peter. The initial balance on the card is 20 euros.
Create a lunch card for Grace. The initial balance on the card is 30 euros.
Peter eats a special
Grace eats a regular lunch
Print out the balance on each card (on separate lines, with the name of the owner at the beginning of the line)
Peter deposits 20 euros
Grace eats the special
Print out the balance on each card (on separate lines, with the name of the owner at the beginning of the line)
Peter eats a regular lunch
Peter eats a regular lunch
Grace deposits 50 euros
Print out the balance on each card (on separate lines, with the name of the owner at the beginning of the line)
Body of the main program

peters_card = LunchCard(20)
graces_card = LunchCard(30)
# the rest of your main function
Your main function should print out exactly the following:

Sample output
Peter: The balance is 15.4 euros
Grace: The balance is 27.4 euros
Peter: The balance is 35.4 euros
Grace: The balance is 22.8 euros
Peter: The balance is 30.2 euros
Grace: The balance is 72.8 euros
"""


# Write your solution here:
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"

    def eat_lunch(self):
        lunch_price = 2.60
        if self.balance >= lunch_price:
            self.balance -= lunch_price

    def eat_special(self):
        special_price = 4.60
        if self.balance >= special_price:
            self.balance -= special_price

    def deposit_money(self, amount: float):
        if amount >= 0:
            self.balance += amount
        else:
            raise ValueError("You cannot deposit an amount of money less than zero")


peters_card = LunchCard(20)
graces_card = LunchCard(30)

peters_card.eat_special()
graces_card.eat_lunch()

print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")

peters_card.deposit_money(20)
graces_card.eat_special()

print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")

peters_card.eat_lunch()
peters_card.eat_lunch()

graces_card.deposit_money(50)

print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")

"""
# Suggested solution

class LunchCard:
    def __init__(self, balance):
        self.balance = balance
 
    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"
 
    def eat_lunch(self):
        if self.balance >= 2.6:
            self.balance -= 2.6
 
    def eat_special(self):
        if self.balance >= 4.6:
            self.balance -= 4.6
 
    def deposit_money(self, money: float):
        if money < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        self.balance += money
 
peters_card = LunchCard(20)
graces_card = LunchCard(30)
 
peters_card.eat_special()
graces_card.eat_lunch()
 
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")
 
peters_card.deposit_money(20)
graces_card.eat_special()
 
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")
 
peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
 
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")


#Review
My solution results in the same output, suggested one increments
seconds first, and then checks for rollover to reset if necessary which
makes the code a bit more compact. 
"""
