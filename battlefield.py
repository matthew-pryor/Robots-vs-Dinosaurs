from fleet import Fleet
from herd import Herd

class Battlfield:

    def __init__(self):
        
        self.team_robo = Fleet()

        self.team_dino = Herd()

    def run_game(self): #void - this should be a 'while statement' to keep the game running in a loop. Should be nothing but modifiers.
        
        self.display_welcome()

        self.battle()

        self.display_winners()

    def display_welcome(self): #void - displays when the game is ran, one and done.
        
        print('************************************************************************************************************************************************')
        print('WELCOME TO THE ONLY BATTLE ROYALE THAT MATTERS WHERE THE BETS DONT MATTER AND WOULD BE KEPT BY THE HOUSE ANYWAYS!')
        print()
        print(f"Fighting for Team Dynomite we've got {self.team_dino.dino_1.name}, {self.team_dino.dino_2.name}, and {self.team_dino.dino_3.name}!")
        print()
        print(f"Fighting for Team Robo Dynasty we've got {self.team_robo.robo_1.name}, {self.team_robo.robo_2.name}, and {self.team_robo.robo_3.name}!")
        print('************************************************************************************************************************************************')
    
    def battle(self): #void - ran after the display and initiates the first turn. This is where the turns alternated between one another.

        self.game_winner = False

        self.dino_turn_now = True

        print("Team Dinomyte always goes first since they were technically on the Earth first and still don't have lasers... it's only fair.")

        while self.game_winner is False:

            while self.dino_turn_now == True:

                if ((len(self.team_robo.fleet) == 0) or (len(self.team_dino.herd) == 0)):

                    self.game_winner = True
                    self.dino_turn_now = False

                else:
                    
                    self.dino_turn()
                    self.dino_turn_now = False


            while self.dino_turn_now == False:

                if ((len(self.team_robo.fleet) == 0) or (len(self.team_dino.herd) == 0)):

                    self.game_winner = True
                    self.dino_turn_now = True
            
                else:
                    
                    self.robo_turn()
                    self.dino_turn_now = True

    def dino_turn(self): #void display the current status of the herd (who is left, what their health is at, and their attack_power)
        
        print("Current status of Team Dynomite:")

        for dino in self.team_dino.herd:

            print(f'Press {self.team_dino.herd.index(dino)} to select {dino.name} (Hitpoints: {dino.health}, Attack Power: {dino.dino_attack_power})')

        self.show_dino_opponent_options()

        print('************************************************************************************************************************************************')

    def robo_turn(self): #void

        print("Current status of Team Robo Dynasty:")

        for robot in self.team_robo.fleet:

            print(f'Press {self.team_robo.fleet.index(robot)} to select {robot.name} (Hitpoints: {robot.health}, Attack Power: {robot.robo_attack_power})')

        self.show_robo_opponent_options()

        print('************************************************************************************************************************************************')

    def show_dino_opponent_options(self): #void

        dino_player_input = input('Please select a dinosaur to attack with: ')

        dino_player_input_index = int(dino_player_input)

        attacker = self.team_dino.herd[dino_player_input_index]

        print("Current status of Team Robo Dynasty:")

        for robot in self.team_robo.fleet:

            print(f'Press {self.team_robo.fleet.index(robot)} to select {robot.name} (Hitpoints: {robot.health}, Attack Power: {robot.robo_attack_power})')

        dino_player_target_input = input('Please select a robot to attack with your prehistoric anger: ')

        dino_player_target_input_index = int(dino_player_target_input)

        target = self.team_robo.fleet[dino_player_target_input_index]

        attacker.attack(target)

        for robo in self.team_robo.fleet:

            if robo.health <= 0:

                self.team_robo.fleet.remove(robo)

    def show_robo_opponent_options(self):
        
        robo_player_input = input('Please select a robot to attack with: ')

        robo_player_input_index = int(robo_player_input)

        attacker = self.team_dino.herd[robo_player_input_index]

        print("Current status of Team Dinomyte:")

        for dino in self.team_dino.herd:

            print(f'Press {self.team_dino.herd.index(dino)} to select {dino.name} (Hitpoints: {dino.health}, Attack Power: {dino.dino_attack_power})')

        robo_player_target_input = input('Please select a dinosaur to attack with your futuristic fury: ')

        robo_player_target_input_index = int(robo_player_target_input)

        target = self.team_dino.herd[robo_player_target_input_index]

        attacker.attack(target)

        for dino in self.team_dino.herd:

            if dino.health <= 0:

                self.team_dino.herd.remove(dino)

    def display_winners(self): #void

        if len(self.team_dino.herd) > 0 and len(self.team_robo.fleet) == 0:

            print('Congratz to Team Dynomite!')

        elif len(self.team_robo.fleet) > 0 and len(self.team_dino.herd) == 0:

            print('Congratz to Team Robo Dynasty')