class Plant:
    def __init__(self, name: str, height: int | float, age: int) -> None:
        self.name = name
        self.height = height
        self.Age = age

    def show(self) -> None:
        name_cap: str = self.name.capitalize()
        print(f"{name_cap}: {self.height}cm, {self.Age} days old")


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
