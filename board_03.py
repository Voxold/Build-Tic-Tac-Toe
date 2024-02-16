# Import player class
from player import Player
from menu import Menu


class Board:
    """Board Class"""

    def __init__(self):
        self.board = [str(i) for i in range (1,10)]

    def display_board(self):
        for i in range(0,9,3):
            print(' | '.join(self.board[i:i+3]))
            if i < 6:
                print('-'*10)
        
    def is_valide_move(self, choice):
        """Solid Principales, Single Risponsability Priciples"""
        return self.board[choice-1].isdigit()

    def update_board(self, choice, symbol):
        if self.is_valide_move == choice:
            self.board[choice-1] = symbol
            return True
        return False

    def reset_board(self):
        self.board = [str(i) for i in range (1,10)]




        