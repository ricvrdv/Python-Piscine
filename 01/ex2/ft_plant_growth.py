#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, plant_age: int):
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def grow(self, amount: float):
        self.height += amount

    def age(self, days: int):
        self.plant_age += days

    def show(self):
        print(
                f"{self.name.capitalize()}:",
                f"{round(self.height, 1)}cm, {self.plant_age} days old")


def main():
    print("=== Garden Plant Growth ===")
    init_height = 25.0
    plant = Plant("rose", init_height, 30)
    plant.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant.grow(0.8)
        plant.age(1)
        plant.show()
    growth = plant.height - init_height
    print(f"Growth this week: {round(growth, 1)}cm")


if __name__ == "__main__":
    main()
