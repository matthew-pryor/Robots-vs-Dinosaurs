from robot import Robot


class Fleet:
    
    def __init__(self) -> None:
        
        self.fleet = []
        self.create_fleet()

    def create_fleet(self): #void

        robo_1 = Robot('Terminator')
        robo_2 = Robot('Robo Cop')
        robo_3 = Robot('Gypsy Danger')

        self.fleet.append(robo_1)
        self.fleet.append(robo_2)
        self.fleet.append(robo_3)