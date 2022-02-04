from fleet import Fleet
from robot import Robot


class Dinosaur:

    def __init__(self, name, attack_power):

        self.name = name
        self.dino_attack_power = attack_power
        self.health = 100

    def attack(self, robot): #void - this is where health is subtracted from the selected robot based on the attack power of the dino.

        robot.health -= self.dino_attack_power

