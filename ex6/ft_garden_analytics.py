class Plant:
    class Analytics:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def show_stats(self) -> None:
            print(f"Stats: {self._grow_calls} grow,",
                  f" {self._age_calls} age,",
                  f" {self._show_calls} show"
                  )

    @staticmethod
    def check_age(age: int) -> None:
        response: bool = age > 365
        print(f"Is {age} days more than a year? -> {response}")

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.p_age = age
        self.analatics = self.Analytics()

    def show(self) -> None:
        self.analatics._show_calls += 1
        print(f"{self.name}: {self.height:.1f}cm, {self.p_age} days old")

    def grow(self, days: int):
        self.analatics._grow_calls += 1
        if (days <= 7):
            self.height += 0.4
        elif (days > 7 and days <= 20):
            self.height += 1.4
        else:
            self.height += 2.3

    def age(self, days: int):
        self.analatics._age_calls += 1
        self.p_age += days

class Flower(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 ) -> None:
        super().__init__(name, height, age)
        self.color = "none"
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
                 ) -> None:
        super().__init__(name, height, age)
        self.diameter = 0
        self.state: bool = False
        self._shade_stat: int = 0

    def produce_shade(self) -> None:
        self.state = True
        self._shade_stat += 1

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


class Seed(Flower):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 ) -> None:
        super().__init__(name, height, age)
        self.seeds: int = 0

    def grow_seeds(self) -> None:
        self.state = True

    def show(self) -> None:
        super().show()
        if self.state:
            self.seeds = 42
        else:
            pass
        print(f"Seeds: {self.seeds}")

def show_stats(plant_obj: Plant) -> None:
    print(f"[statistics for {plant_obj.name}]")
    plant_obj.analatics.show_stats()
    if isinstance(plant_obj, Tree):
        print(f", {plant_obj._shade_stat} shade")
    else:
        pass

def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)

    print()
    print("=== Flower")
    flower: Flower = Flower("rose", 15, 10)
    flower.color = "red"
    flower.show()
    show_stats(flower)
    print(f"[asking the {flower.name} to grow and bloom]")
    flower.grow(10)
    flower.bloom()
    flower.show()
    show_stats(flower)
    
    print()
    print("=== Tree")
    tree: Tree = Tree("oak", 200, 365)
    tree.diameter = 5
    tree.show()
    show_stats(tree)
    print(f"[asking the {tree.name} to produce shade]")
    tree.produce_shade()
    tree.show()
    show_stats(tree)

    print()
    print("=== Seed")
    seed: Seed = Seed("sunflower", 80, 45)
    seed.color = "yellow"
    seed.show()
    show_stats(seed)
    print(f"[make {seed.name} grow, age and bloom]")
    seed.grow(45)
    seed.age(45)
    seed.bloom()
    seed.show()
    show_stats(seed)

    print()
    print("=== Anonymous")


if __name__ == "__main__":
    ft_garden_analytics()