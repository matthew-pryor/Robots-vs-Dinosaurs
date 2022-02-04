from robot import Robot


class Fleet:
    
    def __init__(self) -> None:
        
        self.fleet = []
        self.fleet_names = []
        self.create_fleet()

    def create_fleet(self): #void

        self.robo_1 = Robot('Terminator')
        self.robo_2 = Robot('Robo Cop')
        self.robo_3 = Robot('Gypsy Danger')

        self.fleet.append(self.robo_1)
        self.fleet.append(self.robo_2)
        self.fleet.append(self.robo_3)

        self.fleet_names.append(self.robo_1.name)
        self.fleet_names.append(self.robo_2.name)
        self.fleet_names.append(self.robo_3.name)