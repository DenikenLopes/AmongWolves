
import pygame.image
from code.Const import MENU_OP

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.jpeg')
        self.rect = self.surf.get_rect(left=0,top=0)
        
        #carregar fonte:
        self.font = pygame.font.Font('./fonte/chinese_rocks_rg.otf', 32)
                
    
    def run(self, ):
        self.window.blit(source=self.surf, dest=self.rect)
        
        for i in range(len(MENU_OP)):
            self.text = self.font.render(MENU_OP[i], True, (255,255,255))
            self.tam = self.text.get_rect() #salva largura do texto
            self.x = (800 - self.tam.width)/2 #centralizar
            self.window.blit(self.text, (self.x, 221+40*i)) #width, heigth
            
        pygame.display.flip()