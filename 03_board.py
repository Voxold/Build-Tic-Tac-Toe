
from 00_player import Player

class Board:
    def __init__(self):
        self.board = [str(i) for i in range (1,10)]

    def display_board(self):
        for i in range(0,9,3):
            print(' | '.join(self.board[i:i+3]))
            if i < 6:
                print('-'*10)
        
    
    def update_board(self):
        user = input('Put your symbol :')
        if user == self.board:
            display_board(self)
            

    def reset_board(self):
        pass

lis = [1,2,3,4,5,6,7,8,9]