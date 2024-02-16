class Menu():
    """We havn't __init__ cuz we dont have attribuets"""
    def main_menu(self):
        main_menu = """Welcome to X-O game
                        1 - Start Game
                        2 - Quit Game"""
        while True:
            choice = int(input(main_menu))
            if choice == 1 or choice == 2:
                return choice
                break
            print('Invalide, please choose between 1 and 2 :')
        
                
    def end_menu(self):
        end_menu =  """Welcome to X-O game
                        1 - Start Game
                        2 - Quit Game"""
        while True:
            choice = int(input(end_menu))
            if choice == 1 or choice == 2:
                return choice
                break
            print('Invalide, please choose between 1 and 2 :')