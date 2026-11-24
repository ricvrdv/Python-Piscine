#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str):
        self.name = name
        self._height = 15.0
        self._age = 10
        print("Plant created:", end=" ")
        self.show()

    def show(self):
        print(
                f"{self.name.capitalize()}:",
                f"{round(self._height, 1)}cm, {self._age} days old")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float):
        if height < 0:
            print(
                    f"{self.name.capitalize()}: ",
                    "Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm")

    def set_age(self, age: int):
        if age < 0:
            print(
                    f"{self.name.capitalize()}: ",
                    "Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days")


def main():
    print("=== Garden Security System ===")
    plant1 = Plant("rose")
    print()
    plant1.set_height(25.0)
    plant1.set_age(30)
    print()
    plant1.set_height(-3)
    plant1.set_age(-1)
    print()
    print("Current state:", end=" ")
    plant1.show()


if __name__ == "__main__":
    main()
