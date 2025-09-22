from typing import List


class Animal:
    alive: List["Animal"] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        animals_info = []
        for animal in Animal.alive:
            animals_info.append(
                f"{{Name: {animal.name}, "
                f"Health: {animal.health}, "
                f"Hidden: {animal.hidden}}}"
            )
        return "[" + ", ".join(animals_info) + "]"

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if not isinstance(other, Herbivore):
            return
        if other.hidden:
            return
        other.health -= 50
        if other.health <= 0:
            other.health = 0
            other.die()
