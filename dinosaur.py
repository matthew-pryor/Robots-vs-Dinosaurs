from fleet import Fleet
from robot import Robot


class Dinosaur:

    def __init__(self, name, attack_power):

        self.name = name
        self.dino_attack_power = attack_power
        self.health = 100

    def attack(self, robot, robot_list): #void - this is where health is subtracted from the selected robot based on the attack power of the dino.

        robot.health -= self.dino_attack_power

        if robot.health > 0:

            print(f"Solid hit! {robot.name} is now down to {robot.health} hitpoints.")

        else:

            robot_list.fleet.remove(robot)

            print(f"That's a lot of damage! Looks like {robot.name} is out of commission!")

            robot_list.fleet_names.remove(robot.name)