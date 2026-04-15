class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.p_age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.p_age} days old")

    def grow(self, days: int):
        if (days <= 7):
            self.height += 0.4
        elif (days > 7 and days <= 20):
            self.height += 1.4
        else:
            self.height += 2.3

    def age(self, days: int):
        self.p_age += days


class Flower(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 color: str
                 ) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.state: bool = False

    def bloom(self) -> None:
        self.state = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if (self.state):
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 d: float
                 ) -> None:
        super().__init__(name, height, age)
        self.diameter = d
        self.state: bool = False

    def produce_shade(self) -> None:
        self.state = True

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.diameter:.1f}cm")
        if self.state:
            string: str = f"Tree {self.name} now produces a shade of"
            height_str: str = f"{self.height:.1f}cm long and"
            width: str = f"{self.diameter:.1f}cm wide."
            print(f"{string} {height_str} {width}")
        else:
            pass


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 harverst_season: str
                 ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harverst_season.capitalize()
        self.nutritional_value = 0
        self.state: bool = False

    def grow(self, days: int):
        super().grow(days)
        self.nutritional_value += (days // 2)

    def age(self, days: int):
        super().age(days)
        self.nutritional_value += (days // 2)

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower: Flower = Flower("rose", 15, 10, "red")
    flower.show()
    print(f"[asking the {flower.name} to bloom]")
    flower.bloom()
    flower.show()

    print()
    print("=== Tree")
    tree: Tree = Tree("oak", 200, 365, 5)
    tree.show()
    print(f"[asking the {tree.name} to produce shade]")
    tree.produce_shade()
    tree.show()

    print()
    print("=== Vegetable")
    veg: Vegetable = Vegetable("tomato", 5, 10, "april")
    veg.show()
    print(f"[make {veg.name} grow and age for {veg.p_age} days]")
    veg.grow(20)
    veg.age(20)
    veg.show()

if __name__ == "__main__":
    ft_plant_types()

