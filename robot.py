from weapon import Weapon


class Robot:

    def __init__(self, name):

        self.name = name
        self.health = 100
        weapon = Weapon('Pulse Rifle', 20)
        self.attack_power = weapon.attack_power

    def attack(self, dinosaur): #void
        pass