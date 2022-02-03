


from typing_extensions import Self


class Dinosaur:

    def __init__(self, name, attack_power) -> None:
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot): #void
        pass