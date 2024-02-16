# Import player class
from player_01 import Player
from menu_02 import Menu
from board_03 import Board
import os


def os_clear():
    """Clear Screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

class Game:
    """Composition Relation"""
    def __init__(self):
        self.players = [Player(),Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.main_menu()
        if choice == 1:
            # this is method for playes setup >> name and symbol
            self.setup_players()
            # this is play game new method
            self.play_game()
        else:
            # quit game mathod
            slef.quit_game()


    def setup_players(self):
        for number,player in enumerate(self.players, start=1):
            print(f'Player{number}, Enter your details :')
            player.choose_name()
            player.choose_symbol()
            os_clear()

    def play_game(self):
        while True:
            # Creat method that give turn to player
            self.play_turn()
            # Creat 2 method that check win pr draw
            if self.check_win() or self.check_draw :
                choice =  self.Menu.end_menu()
                if choice == '1':
                    # create method that allow olayers to restar game
                    self.restart_game()
                else:
                    self.quit_game()
                    break
                
    def play_turn():
        pass

    def quit_game(self):
        print('Thank you for playing!')