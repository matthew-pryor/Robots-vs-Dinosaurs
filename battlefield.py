from fleet import Fleet
from herd import Herd

class Battlfield:

    def __init__(self):
        
        Fleet()

        Herd()

    def run_game(self): #void - this should be a 'while statement' to keep the game running in a loop. Should be nothing but modifiers.
        
        self.display_welcome()
        
        game_winner = False

        while game_winner is False:

            self.battle()

    def display_welcome(self): #void - displays when the game is ran, one and done.

        print('WELCOME TO THE ONLY BATTLE ROYALE THAT MATTERS WHERE THE BETS DONT MATTER AND WOULD BE KEPT BY THE HOUSE ANYWAYS!')

    def battle(self): #void - ran after the display and initiates the first turn.

        pass

    def dino_turn(self): #void

        self.show_dino_opponent_options()

    def robo_turn(self): #void

        self.show_robo_opponent_options()

    def show_dino_opponent_options(self): #void

        self.herd = Herd()

    def show_robo_opponent_options(self): #void

        self.fleet = Fleet()

    def display_winners(self): #void

        pass