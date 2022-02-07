from random import randint
from robot import Robot
from weapon import Weapon


class Fleet:
    
    def __init__(self) -> None:
        
        self.fleet = []
        self.create_fleet()

    def create_fleet(self): #void

        self.robo_1 = Robot('Cyberman Cyril', Weapon('Pulse Rifle', randint(39, 50)))
        self.robo_2 = Robot('Victor the Venerable Dreadnaught', Weapon('Power Fist', randint(50, 61)))
        self.robo_3 = Robot('Gypsy Danger', Weapon('Chainsword', randint(45, 75)))

        self.fleet.append(self.robo_1)
        self.fleet.append(self.robo_2)
        self.fleet.append(self.robo_3)