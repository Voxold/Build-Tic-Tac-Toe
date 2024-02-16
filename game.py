# Import player class
from player import Player
from menu import Menu
from board import Board
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
            self.quit_game()


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
        check_lists =[[0,1,2],[3,4,5],[6,7,8],  # rows
                     [0,3,6,],[1,4,7,],[2,5,8], # colums
                     [0,4,8],[2,4,6]]           # diagonals
        
        for combo in check_lists: #[0,1,2]
            if (self.board.board[combo[0]] == self.board.board[combo[1]]
                == self.board.board[combo[2]]):
                return True
            else:
                return False
    
    def check_draw(self):
        """ 4 """
        # we use all() of iterable method to return true if all true
        return all(not cell.isdigit() for cell in self.board.board)

    def restart_game(self):
        """ 5 """
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

    def quit_game(self):
        """ 6 """
        print('Thank you for playing!')

game = Game()