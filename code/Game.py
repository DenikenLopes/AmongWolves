import pygame
from code.Menu import Menu
from code.Level import Level
from code.Const import WIDTH, HEIGHT, MENU_OP

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIDTH, HEIGHT))
    
    def run(self):   
                
        while True:
            
            menu = Menu(self.window)    
            return_menu = menu.run()
            
            if return_menu == MENU_OP[0]:
                level = Level(self.window)
                level.run()
            if return_menu == MENU_OP[1]:
                print("fase salva")
            if return_menu == MENU_OP[2]:
                pygame.quit()
                quit()
            else:
                pass