from random import randint
from weapon import Weapon


class Robot:

    def __init__(self, name, weapon):

        self.name = name
        self.health = 100
        self.weapon = weapon
        self.robo_attack_power = weapon.weapon_attack_power

    def attack(self, dinosaur): #void

        dinosaur.health -= self.robo_attack_power

        if dinosaur.health > 0:

            print(f"Solid hit! {dinosaur.name} is now down to {dinosaur.health} hitpoints.")

        else:

            print(f"That's a lot of calculated destruction! Blood and scales are everywhere! Looks like {dinosaur.name} is finally extinct!")