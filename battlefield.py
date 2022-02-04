from fleet import Fleet
from herd import Herd

class Battlfield:

    def __init__(self):
        
        self.team_robo = Fleet()

        self.team_dino = Herd()

    def run_game(self): #void - this should be a 'while statement' to keep the game running in a loop. Should be nothing but modifiers.
        
        self.display_welcome()
        
        game_winner = False

        while game_winner is False:

            self.battle()

    def display_welcome(self): #void - displays when the game is ran, one and done.
        
        print('************************************************************************************************************************************************')
        print('WELCOME TO THE ONLY BATTLE ROYALE THAT MATTERS WHERE THE BETS DONT MATTER AND WOULD BE KEPT BY THE HOUSE ANYWAYS!')
        print()
        print(f"Fighting for Team Dynomite we've got {self.team_dino.dino_1.name}, {self.team_dino.dino_2.name}, and {self.team_dino.dino_3.name}!")
        print()
        print(f"Fighting for Team Robo Dynasty we've got {self.team_robo.robo_1.name}, {self.team_robo.robo_2.name}, and {self.team_robo.robo_3.name}!")
        print('************************************************************************************************************************************************')
    
    def battle(self): #void - ran after the display and initiates the first turn.

        pass

    def dino_turn(self): #void

        self.show_dino_opponent_options()

    def robo_turn(self): #void

        self.show_robo_opponent_options()

    def show_dino_opponent_options(self): #void

        self.team_dino.dino_1.attack(self.team_robo.robo_1, self.team_robo)

    def show_robo_opponent_options(self): #void

        self.team_robo.robo_1.attack(self.team_dino.dino_1, self.team_dino)

    def display_winners(self): #void

        pass