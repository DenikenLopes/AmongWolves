
import pygame.image
from code.Const import MENU_OP, COR_YELLOW, COR_WHITE, WIDTH

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.jpeg')
        self.rect = self.surf.get_rect(left=0,top=0)       
        #carregar fonte:
        self.font = pygame.font.Font('./fonte/chinese_rocks_rg.otf', 32)
                
    
    def run(self):
        
        pos = 0
        pygame.mixer.init()
        music = pygame.mixer.Sound('./audio/Bosch_Garden.mp3')
        music.play(-1)
        
        while True:        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if pos < len(MENU_OP)-1:
                            pos += 1
                        else:
                            pos = 0
                    if event.key == pygame.K_UP:
                        if pos > 0:
                            pos -= 1
                        else:
                            pos = len(MENU_OP)-1
                    if event.key == pygame.K_RETURN and pos == 0:
                        print('acessando fase 1')
                        pass # acesso a fase do game
                    if event.key == pygame.K_RETURN and pos == 2:
                        pygame.quit()
                        quit()

                    
        
            self.window.blit(source=self.surf, dest=self.rect)
        
            for i in range(len(MENU_OP)):
                
                if i == pos:
                    select = COR_YELLOW
                else:
                    select = COR_WHITE
                    
                self.text = self.font.render(MENU_OP[i], True, (select))
                self.tam = self.text.get_rect() #salva largura do texto
                self.x = (WIDTH - self.tam.width)/2 #centralizar
                self.window.blit(self.text, (self.x, 221+40*i)) #width, heigth
                
            pygame.display.flip()