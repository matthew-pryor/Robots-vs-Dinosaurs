from fleet import Fleet
from herd import Herd

class Battlfield:

    def __init__(self):
        
        self.team_robo = Fleet()

        self.team_dino = Herd()

    def run_game(self): #void - this should be a 'while statement' to keep the game running in a loop. Should be nothing but modifiers.
        
        self.display_welcome()
        
        self.game_winner = False
        self.dino_turn_now = True
        self.robo_turn_now = False

        while self.game_winner is False:

            self.battle()

            if ((len(self.team_dino.herd) < 0) or (len(self.team_robo) < 0)):

                self.game_winner = True

            else:
                
                self.game_winner = False

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

        self.dino_turn_now = True
        self.robo_turn_now = False

        while self.dino_turn_now == True and self.robo_turn_now == False:

            self.dino_turn()

            self.dino_turn_now = False
            self.robo_turn_now = True

        while self.dino_turn_now == False and self.robo_turn_now == True:

            self.robo_turn()

            self.dino_turn_now = True
            self.robo_turn_now = False

    def dino_turn(self): #void display the current status of the herd (who is left, what their health is at, and their attack_power)
        
        print("Current status of Team Dynomite:")

        count = 0

        while (self.team_dino.dino_1 in self.team_dino.herd) and count == 0:

            print(f'Press {self.team_dino.herd.index(self.team_dino.dino_1)} to select Toby (Hitpoints: {self.team_dino.dino_1.health}, Attack Power: {self.team_dino.dino_1.dino_attack_power})')

            count += 1

        count = 0

        while (self.team_dino.dino_2 in self.team_dino.herd) and count == 0:
            
            print(f'Press {self.team_dino.herd.index(self.team_dino.dino_2)} to select Moo (Hitpoints: {self.team_dino.dino_2.health}, Attack Power: {self.team_dino.dino_2.dino_attack_power})')

            count += 1

        count = 0

        while (self.team_dino.dino_3 in self.team_dino.herd) and count == 0:
            
            print(f'Press {self.team_dino.herd.index(self.team_dino.dino_3)} to select Jaxson (Hitpoints: {self.team_dino.dino_3.health}, Attack Power: {self.team_dino.dino_3.dino_attack_power})')

            count += 1

        self.show_dino_opponent_options()

    def robo_turn(self): #void

        print("Current status of Team Robo Dunasty:")

        count = 0

        while (self.team_robo.robo_1 in self.team_robo.fleet) and count == 0:

            print(f'Press {self.team_robo.fleet.index(self.team_robo.robo_1)} to select Toby (Hitpoints: {self.team_robo.robo_1.health}, Attack Power: {self.team_robo.robo_1.robo_attack_power})')

            count += 1

        count = 0

        while (self.team_robo.robo_2 in self.team_robo.fleet) and count == 0:
            
            print(f'Press {self.team_robo.fleet.index(self.team_robo.robo_1)} to select Moo (Hitpoints: {self.team_robo.robo_2.health}, Attack Power: {self.team_robo.robo_3.robo_attack_power})')

            count += 1

        count = 0

        while (self.team_robo.robo_3 in self.team_robo.fleet) and count == 0:
            
            print(f'Press {self.team_robo.fleet.index(self.team_robo.robo_3)} to select Jaxson (Hitpoints: {self.team_robo.robo_3.health}, Attack Power: {self.team_robo.robo_3.robo_attack_power})')

            count += 1

        self.show_robo_opponent_options()

    def show_dino_opponent_options(self): #void

        dino_player_input = input('Please select a dinosaur to attack with: ')

        dino_player_input_index = int(dino_player_input)

        attacker = self.team_dino.herd[dino_player_input_index]

        print("Current status of Team Robo Dunasty:")

        count = 0

        while (self.team_robo.robo_1 in self.team_robo.fleet) and count == 0:

            print(f'Press {self.team_robo.fleet.index(self.team_robo.robo_1)} to select Toby (Hitpoints: {self.team_robo.robo_1.health}, Attack Power: {self.team_robo.robo_1.robo_attack_power})')

            count += 1

        count = 0

        while (self.team_robo.robo_2 in self.team_robo.fleet) and count == 0:
            
            print(f'Press {self.team_robo.fleet.index(self.team_robo.robo_1)} to select Moo (Hitpoints: {self.team_robo.robo_2.health}, Attack Power: {self.team_robo.robo_3.robo_attack_power})')

            count += 1

        count = 0

        while (self.team_robo.robo_3 in self.team_robo.fleet) and count == 0:
            
            print(f'Press {self.team_robo.fleet.index(self.team_robo.robo_3)} to select Jaxson (Hitpoints: {self.team_robo.robo_3.health}, Attack Power: {self.team_robo.robo_3.robo_attack_power})')

            count += 1

        dino_player_target_input = input('Please select a robot to attack with your prehistoric anger: ')

        dino_player_target_input_index = int(dino_player_target_input)

        target = self.team_robo.fleet[dino_player_target_input_index]

        self.team_dino.herd[attacker].attack(self.team_robo.fleet[target], self.team_robo.fleet)

    def show_robo_opponent_options(self):
        pass

    def display_winners(self): #void

        if ((len(self.team_dino.herd)) > 0):

            print('Congratz to Team Dynomite!')

        else:

            print('Congratz to Team Robo Dynasty')

    def test(self):

        print("Current status of Team Dynomite:")

        count = 0

        while (self.team_dino.dino_1 in self.team_dino.herd) and count == 0:

            print(f'Press {self.team_dino.herd.index(self.team_dino.dino_1)} to select Toby ({self.team_dino.dino_1.health}, {self.team_dino.dino_1.dino_attack_power})')

            count += 1

        count = 0

        while (self.team_dino.dino_2 in self.team_dino.herd) and count == 0:
            
            print(f'Press {self.team_dino.herd.index(self.team_dino.dino_2)} to select Moo ({self.team_dino.dino_2.health}, {self.team_dino.dino_2.dino_attack_power})')

            count += 1

        count = 0

        while (self.team_dino.dino_3 in self.team_dino.herd) and count == 0:
            
            print(f'Press {self.team_dino.herd.index(self.team_dino.dino_3)} to select Jaxson ({self.team_dino.dino_3.health}, {self.team_dino.dino_3.dino_attack_power})')

            count += 1