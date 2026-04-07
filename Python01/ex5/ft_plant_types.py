class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.Age = age

    def show(self) -> None:
        name_cap: str = self.name.capitalize()
        print(f"{name_cap}: {self.height:.1f}cm, {self.Age} days old")

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
    

class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.state: bool = False

    def show_plant(self):
        if (self.state == False):
            print(f"{self.name.capitalize()} has not bloomed yet")
            print(f"[asking the {self.name} to bloom]")
            self.state = True
        elif (self.state == True):
            print(f"{self.name.capitalize()} is blooming beautifully!")

    def bloom(self):
        super().show()
        self.show_plant()


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, d: float):
        super().__init__(name, height, age)
        self.diameter = d
        self.state: bool = False

    def show_tree(self):
        if (self.state == False):
            print(f"[asking the {self.name} to produce shade]")
            self.state = True
        elif (self.state == True):
            string: str = f"Tree {self.name.capitalize()} now produces a shade of"
            height_str: str = f"{self.height:.1f}cm long and"
            width: str = f"{self.diameter:.1f}cm wide."
            print(f"{string} {height_str} {width}")

    def produce_shade(self):
        super().show()
        self.show_tree()        


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harverst_season: str):
        super().__init__(name, height, age)
        self.harvest_season = harverst_season
        self.state: bool = False

    def show_vegetable():
        

    def bloom(self):
        super().show()
        if (self.state == False):
            print(f"{self.name.capitalize()} has not bloomed yet")
            print(f"[asking the {self.name} to bloom]")
            self.state = True
        elif (self.state == True):
            print(f"{self.name.capitalize()} is blooming beautifully!")
