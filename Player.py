class Player():
    def __init__(self):
        self.name = ''
        self.symbole = ''
    def choose_name(self):
        name = input('Enter your name (Letters only) :')
        while True:
            if name.isalpha() == True:
                self.name = name
                break
            print('Invalide, please use letters only!')
        
    def choose_symbol(self):
        while True:
            symbol = input(f'{self.name}, Choose your symbol, (a single letter) :')
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print('Invalide, please use one letters only!')




