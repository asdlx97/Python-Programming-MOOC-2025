"""
NB: Some exercises have multiple parts, and you can receive points for the different parts separately. You can submit a partially completed exercise by choosing 'Submit Solution' from the menu next to the button for executing tests .

The exercise template contains an outline for a class named Money. This exercise asks you to implement some additional methods and to fix some small problems in the template.

Fix the string representation

The __str__ method in the class definition doesn't work quite right. Given the following two Money objects, the latter is printed out wrong:

e1 = Money(4, 10)
e2 = Money(2, 5)  # two euros and five cents

print(e1)
print(e2)
Sample output
4.10
2.5
Please fix the method so that it prints out

Sample output
4.10 eur
2.05 eur
Equal amounts

Please define a new method named __eq__(self, another) which allows you to use the == comparison operator on Money objects. You can test your implementation with the following code:

e1 = Money(4, 10)
e2 = Money(2, 5)
e3 = Money(4, 10)

print(e1)
print(e2)
print(e3)
print(e1 == e2)
print(e1 == e3)
Sample output
4.10 eur
2.05 eur
4.10 eur
False
True
Other comparison operators

Please implement the appropriate methods for the comparison operators <, > and !=.

e1 = Money(4, 10)
e2 = Money(2, 5)

print(e1 != e2)
print(e1 < e2)
print(e1 > e2)
Sample output
True
False
True
Addition and subtraction

Please implement the addition and subtraction operators + and - for Money objects. Both should return a new object of type Money. Neither the object itself nor the object passed as an argument should be changed as a result.

NB: the value of a Money object cannot be negative. If an attempt to subtract would result in a negative result, the method should raise a ValueError exception.

e1 = Money(4, 5)
e2 = Money(2, 95)

e3 = e1 + e2
e4 = e1 - e2

print(e3)
print(e4)

e5 = e2-e1
Sample output
7.00 eur
1.10 eur
Traceback (most recent call last):
File "money.py", line 416, in
e5 = e2-e1
File "money.py", line 404, in sub
raise ValueError(f"a negative result is not allowed")
ValueError: a negative result is not allowed
The value must not be directly accessible

The class still has a small integrity issue. The user can "cheat" by accessing the attributes directly and changing the value stored in the Money object:

print(e1)
e1.euros = 1000
print(e1)

Sample output
4.05 eur
1000.05 eur
Please encapsulate the implementation of the attributes defined in the class so that the cheat used above is not possible. The class should have no public attributes, and no getter or setter methods for the euros or the cents.
"""


# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{float(self._euros) + float(self._cents/100):0.2f} eur"

    def __eq__(self, another):
        return (self._euros, self._cents) == (another._euros, another._cents)

    def __ne__(self, another):
        return (self._euros, self._cents) != (another._euros, another._cents)

    def __lt__(self, another):
        return (float(self._euros) + float(self._cents / 100)) < (
            float(another._euros) + float(another._cents / 100)
        )

    def __gt__(self, another):
        return (float(self._euros) + float(self._cents / 100)) > (
            float(another._euros) + float(another._cents / 100)
        )

    def __add__(self, another):
        added = Money(self._euros + another._euros, self._cents + another._cents)
        return added

    def __sub__(self, another):
        if (
            float(self._euros - another._euros)
            + float(self._cents - another._cents) / 100
            < 0
        ):
            raise ValueError("Cannot be negative!")

        substracted = Money(self._euros - another._euros, self._cents - another._cents)
        return substracted


if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2 - e1

"""
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
 
    def __str__(self):
        # f-string has a handy feature for adding leading zeros:
        # :02d for example means, that output has at least 2 digit
        return f"{self.__euros}.{self.__cents:02d} eur"
 
    # Helper method for returning the value in cents
    # --> makes the comparisons easier
    def __value(self):
        return self.__euros * 100 + self.__cents
 
    # Another helper method which converts cents to value
    def __set_value(self, cents: int):
        self.__euros = cents // 100
        self.__cents = cents - self.__euros * 100
 
    def __eq__(self, other: "Money"):
        return self.__value() == other.__value()
 
    def __lt__(self, other: "Money"):
        return self.__value() < other.__value()
 
    def __gt__(self, other: "Money"):
        return self.__value() > other.__value()
 
    def __ne__(self, other: "Money"):
        return self.__value() != other.__value()
 
    def __add__(self, other: "Money"):
        msum = Money(0,0)
        msum.__set_value(self.__value() + other.__value())
        return msum
 
    def __sub__(self, other: "Money"):
        difference = self.__value() - other.__value()
        if difference < 0:
            raise ValueError("a negative result is not allowed")
        dmoney = Money(0,0)
        dmoney.__set_value(self.__value() - other.__value())
        return dmoney
 

#Review
My solution results in the same output, the suggested one uses two 
helper functions: one to return the tuple values in cents only and another one
to convert the cents bacl to to the tuple values. I just divide the cents
while defining the comparison methods. The suggested one looks a bit cleaner I must say.

"""
