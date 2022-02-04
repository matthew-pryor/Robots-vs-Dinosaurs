from weapon import Weapon


class Robot:

    def __init__(self, name):

        self.name = name
        self.health = 100
        weapon = Weapon('Pulse Rifle', 20)
        self.robo_attack_power = weapon.weapon_attack_power

    def attack(self, dinosaur): #void

        pass