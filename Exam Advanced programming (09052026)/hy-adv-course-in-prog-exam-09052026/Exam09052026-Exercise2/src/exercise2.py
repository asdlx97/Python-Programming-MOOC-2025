# Write your solution to exercise 2 here


class Car:
    __current_year = 0

    def __init__(self, brand: str, purchase_year: int, purchase_price: int):
        self.__brand = brand
        self.__purchase_year = purchase_year
        self.__purchase_price = purchase_price
        self.__total_kilometers = 0
        self.__total_costs = float(0)
        if purchase_year > Car.__current_year:
            Car.__current_year = purchase_year

    def set_year(self, new_year: int):
        if new_year > Car.__current_year:
            Car.__current_year = new_year

    def drive(self, distance_driven: int, cost_per_kilometer: float):
        self.__total_kilometers += distance_driven
        self.__total_costs += cost_per_kilometer * float(distance_driven)

    def add_expense(self, value: int):
        self.__total_costs += float(value)

    def distance_driven_by_car(self):
        return self.__total_kilometers

    def current_value(self):
        years_old = Car.__current_year - self.__purchase_year
        current_value = self.__purchase_price * (0.85**years_old)
        if years_old == 0:
            return int(self.__purchase_price)
        return int(current_value)

    def cost_per_kilometer(self):
        depreciation = self.__purchase_price - self.current_value()
        costs = self.__total_costs + depreciation
        return (
            float(costs / self.__total_kilometers) if self.__total_kilometers > 0 else 0
        )  # Risk of dividing by 0 here but I assume won't be called before drive()

    def __str__(self):
        return f"{self.__brand}: purchase year {self.__purchase_year}, value {self.current_value()}"


if __name__ == "__main__":
    toyota = Car("Toyota", 2020, 10000)
    print(toyota)
    toyota.drive(100, 0.10)
    print(f"Distance driven with Toyota: {toyota.distance_driven_by_car()}")
    toyota.set_year(2021)
    print(f"Value of Toyota in 2021: {toyota.current_value()}")
    print(toyota)
    print(f"Cost per kilometer for Toyota in 2021: {toyota.cost_per_kilometer()}")
    toyota.set_year(2022)
    print(f"Value of Toyota in 2022: {toyota.current_value()}")
    bmw = Car("BMW", 2023, 20000)
    print(f"Value of Toyota after purchasing BMW: {toyota.current_value()}")
    bmw.drive(200, 0.12)
    bmw.drive(300, 0.13)
    print(f"Distance driven with BMW: {bmw.distance_driven_by_car()}")
    print(f"Cost per kilometer for BMW in 2023: {bmw.cost_per_kilometer()}")
    bmw.add_expense(1000)
    print(
        f"Cost per kilometer for BMW after a 1000 euro service: {bmw.cost_per_kilometer()}"
    )
