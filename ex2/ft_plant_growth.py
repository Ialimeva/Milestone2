class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.p_age = age

    def show(self) -> None:
        print(
            f"{self.name}: "
            f"{self.height:.1f}cm, "
            f"{self.p_age} days old"
        )

    def grow(self, days: int):
        if (days <= 7):
            self.height += 0.4
        elif (days > 7 and days <= 20):
            self.height += 1.4
        else:
            self.height += 2.3

    def age(self, days: int):
        self.p_age += days


def ft_plant_growth() -> None:
    plant = Plant("rose", 25, 30)
    print("=== Garden Plant Growth ===")
    i: int = 0
    days: int = 7
    plant.show()
    initial_height: float = plant.height
    while (i < days):
        plant.grow(days)
        plant.age(1)
        print(f"=== Day {i + 1} ===")
        plant.show()
        i += 1
    print(f"Growth this week: {plant.height - initial_height:.1f}cm")


if __name__ == "__main__":
    ft_plant_growth()
