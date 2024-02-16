# Import player class
from player_01 import Player
from menu_02 import Menu
from board_03 import Board

class Game:
    """Composition Relation"""
    def __init__(self):
        self.players = [Player(),Player()]
        self.board = Board()
        self.menu = Menu()
