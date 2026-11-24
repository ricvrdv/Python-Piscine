#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, st_height: float, st_age: int):
        self.name = name
        self.st_height = st_height
        self.st_age = st_age
        print("Created:", end=" ")
        self.show()

    def grow(self, amount: float):
        self.st_height += amount

    def age(self, days: int):
        self.st_age += days

    def show(self):
        print(
                f"{self.name.capitalize()}:",
                f"{round(self.st_height, 1)}cm, {self.st_age} days old")


def main():
    print("=== Plant Factory Output ===")
    Plant("rose", 25.0, 30)
    Plant("oak", 200.0, 365)
    Plant("cactus", 5.0, 90)
    Plant("sunflower", 80.0, 45)
    Plant("fern", 15.0, 120)


if __name__ == "__main__":
    main()
