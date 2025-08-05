import pygame
from code.Menu import Menu
from code.Const import WIDTH, HEIGHT

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIDTH, HEIGHT))
    
    def run(self):   
        menu = Menu(self.window)    
        menu.run() 