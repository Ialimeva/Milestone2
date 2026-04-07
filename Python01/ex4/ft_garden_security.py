class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._Age = age

    def set_height(self, height: float):
        if (height < 0.0):
            cap_name: str = self.name.capitalize()
            print(f"{cap_name}: Error, height cannot be negative.")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm.")

    def set_age(self, age: int):
        if (age < 0):
            cap_name: str = self.name.capitalize()
            print(f"{cap_name}: Error, age cannot be negative.")
            print("Age update rejected")
        else:
            self._Age = age
            print(f"Age updated: {self._Age} days.")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._Age

    def show(self) -> None:
        name_cap: str = self.name.capitalize()
        height: float = self.get_height()
        age: int = self.get_age()
        print(f"{name_cap}: {height:.1f}cm, {age} days old")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant: Plant = Plant("rose", 100, 23)

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
