class Plant:
    def __init__(self, name: str | None, height: float | None,
                 age: int | None) -> None:
        if name:
            self.name = name.capitalize()
        else:
            self.name = "Unknown Plant"
        if (height is None or height < 0):
            self.__height = 0.0
            print(f"{self.name}: Error, height can't be negative.")
            print(f"Height initialized to {self.__height}cm.")
        else:
            self.__height = height
        if (age is None or age < 0):
            self.__age = 0
            print(f"{self.name}: Error, age can't be negative.")
            print(f"Age initialized to {self.__age} days old.")
        else:
            self.__age = age

    def set_height(self, height: float) -> None:
        if (height < 0.0):
            print(f"{self.name}: Error, height can't be negative.")
            print("Height update rejected")
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm.")

    def set_age(self, age: int) -> None:
        if (age < 0):
            print(f"{self.name}: Error, age can't be negative.")
            print("Age update rejected")
        else:
            self.__age = age
            print(f"Age updated: {self.__age} days.")

    def get_height(self) -> float:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def show(self) -> None:
        height: float = self.get_height()
        age: int = self.get_age()
        print(f"{self.name}: {height:.1f}cm, {age} days old")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant: Plant = Plant("rose", -9, -7)

    print("Plant created: ", end="")
    plant.show()

    print()
    plant.set_height(50)
    plant.set_age(10)

    print()
    plant.set_height(-100)
    plant.set_age(-10)

    print()
    print("Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    ft_garden_security()
