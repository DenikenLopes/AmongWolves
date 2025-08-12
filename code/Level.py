import pygame.image
from code.Const import WIDTH

class Level:
    
    def __init__(self, window):
        self.window = window
        self.camada = []
        self.camada.append(pygame.image.load('./asset/back0.png'))
        self.camada.append(pygame.image.load('./asset/back1.png'))
        self.camada.append(pygame.image.load('./asset/back2.png'))
        self.camada.append(pygame.image.load('./asset/back3.png'))
        self.camada.append(pygame.image.load('./asset/back4.png'))
        self.camada.append(pygame.image.load('./asset/back5.png'))

        #self.surf = camada[0]
        #self.surf = pygame.image.load('./asset/back1.png')
                
    def run(self):
        mov = 0
        while True:
            
                     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT]:
                if mov < 0:
                    mov += 1
                else:                
                    mov = 0
                    
            if teclas[pygame.K_RIGHT]:
                mov -= 1
            
            for i in range(len(self.camada)):
                if i == 4:
                    image = pygame.transform.flip(self.camada[i], False, False)
                else:
                    image = pygame.transform.flip(self.camada[i], True, False)
                    
                self.rect = image.get_rect(left=mov*i,top=0)
                self.window.blit(source=image, dest=self.rect)
                
                image2 = pygame.transform.flip(self.camada[i], False, False)
                self.rect = image2.get_rect(left=WIDTH+mov*i,top=0)
                self.window.blit(source=image2, dest=self.rect)
                            
            
            pygame.display.flip()