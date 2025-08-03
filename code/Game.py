import pygame
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(800, 479))
    
    def run(self):   
        menu = Menu(self.window)    
                
        while True:        
            menu.run()
            pass
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()