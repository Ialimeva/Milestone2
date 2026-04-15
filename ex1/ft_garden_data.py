class Plant:
    def __init__(self,
                 name: str,
                 height: int,
                 age: int
                 ) -> None:
        self.name = name.capitalize()
        self.height = height
        self.Age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.Age} days old")


def ft_garden_data() -> None:
    plant1 = Plant("rose", 25, 30)
    plant2 = Plant("sunflower", 80, 45)
    plant3 = Plant("cactus", 15, 120)
    plants: list[Plant] = [plant1, plant2, plant3]

    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.show()


if __name__ == "__main__":
    ft_garden_data()
