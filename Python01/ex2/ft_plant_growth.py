class Plant:
    def __init__(self, name: str, height: int | float, age: int) -> None:
        self.name = name
        self.height = height
        self.Age = age

    def show(self) -> None:
        name_cap: str = self.name.capitalize()
        print(f"{name_cap}: {self.height}cm, {self.Age} days old")

    def calculation(self, lst: list[float], growth: float, i: int, j: float):
        while i < 7:
            lst[i] = round(self.height, 1) + growth
            i += 1
            growth = growth + j

    def grow(self) -> list[float]:
        lst: list[float] = [0] * 7
        if (self.height <= 10):
            self.calculation(lst, 0.0, 0, 0.4)
        elif (self.height > 10 and self.height <= 30):
            self.calculation(lst, 0.0, 0, 1.5)
        elif (self.height > 30 and self.height <= 50):
            self.calculation(lst, 0.0, 0, 2.8)
        else:
            self.calculation(lst, 0.0, 0, 3.7)
        return (lst)

    def age(self) -> range:
        lst: range = range(self.Age, self.Age + 7, 1)
        return (lst)


def ft_plant_growth() -> None:
    plant = Plant("rose", 500, 30)
    growth: list[float] = plant.grow()
    age: range = plant.age()
    i: int = 0
    print("=== Garden Plant Growth ===")
    while i < 7:
        print(f"=== Day {i + 1} ===")
        plant = Plant("rose", growth[i], age[i])
        plant.show()
        i += 1
    total_growth: int = int(growth[-1] - growth[0])
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
