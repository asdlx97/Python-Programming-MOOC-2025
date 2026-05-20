# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day:int, month:int, year:int):
        self.d = day
        self.m = month
        self.y = year
        self.days = (year*12*30) + (month*30) + day

    def __str__(self):
        return f"{self.d}.{self.m}.{self.y}"

    def __lt__(self, another):
        return self.days < another.days

    def __gt__(self, another):
        return self.days > another.days

    def __ne__(self, another):
        return self.days != another.days

    def __eq__(self, another):
        return self.days == another.days

    def __add__(self, days:int):
        ny = days//360
        print(f"ny: {ny}")
        nm = (days - (ny*360)) // 30
        if self.m + nm >= 12:
            nm = 12-nm
            ny += 1
        print(f"nm: {nm}")
        nd = days - (ny*360) - (nm*30)
        print(f"nd: {nd}")

        return SimpleDate(self.d + nd, nm, self.y + ny)


        



if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)

    d3 = d1 + 3
    d4 = d2 + 400

    print(d1)
    print(d2)
    print(d3)
    print(d4)