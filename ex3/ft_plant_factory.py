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

def ft_plant_factory() -> None:
    plant1: Plant = Plant("rose", 25.0, 30)
    plant2: Plant = Plant("oak", 200.0, 365)
    plant3: Plant = Plant("cactus", 5.0, 90)
    plant4: Plant = Plant("sunflower", 80.0, 40)
    plant5: Plant = Plant("fern", 15.0, 120)

    plants: list[Plant] = [plant1, plant2, plant3, plant4, plant5]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    ft_plant_factory()
