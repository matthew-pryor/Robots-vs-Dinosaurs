from weapon import Weapon


class Robot:

    def __init__(self, name):

        self.name = name
        self.health = 100
        weapon = Weapon('Pulse Rifle', 20)
        self.robo_attack_power = weapon.weapon_attack_power

    def attack(self, dinosaur, dinosaur_list): #void

        dinosaur.health -= self.robo_attack_power

        if dinosaur.health > 0:

            print(f"Solid hit! {dinosaur.name} is now down to {dinosaur.health} hitpoints.")

        else:

            dinosaur_list.herd.remove(dinosaur)

            print(f"That's a lot of damage! Looks like {dinosaur.name} is out of commission!")
            
            dinosaur_list.herd_names.remove(dinosaur.name)