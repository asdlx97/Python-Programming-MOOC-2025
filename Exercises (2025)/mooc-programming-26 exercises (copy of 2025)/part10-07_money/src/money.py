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
