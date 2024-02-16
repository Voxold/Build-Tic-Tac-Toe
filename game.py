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
        """1/2/3/4/5/6 Methods"""
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

    def play_turn(self):
        """ 1 """
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"player{player.choose_name}'s turn! ({player.choose_symbol})")
        while True:
            try:
                cell_choice = int(input('choose a cell (1-9) :'))
                if 1<=cell_choice<=9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print('Invalide Move!')
            except ValueError:
                print('Please entre number between (1-9)!')
        #switch player
        self.switch_player()
    
    
    def switch_player(self):
        """ 2 """
        self.current_player_index = 1 - self.current_player_index
    
    def check_win(self):
        """ 3 """
        pass
    def check_draw(self):
        """ 4 """
        pass
    def restart_game(self):
        """ 5 """
        pass
    def quit_game(self):
        """ 6 """
        print('Thank you for playing!')