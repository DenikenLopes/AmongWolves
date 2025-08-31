from code.Entity import Entity
from code.Const import WIDTH, SPEED
import pygame


class Background(Entity):
    
    def __init__(self, name, position):
        super().__init__(name, position)
        self.speed = SPEED.get(name, 2)
    
    def move(self, direction=0):
   
        # desloca conforme direção
        self.rect.x -= self.speed * direction

        # reposiciona ao sair da tela
        if self.rect.right <= 0:  # saiu pela esquerda
            self.rect.left = WIDTH
        elif self.rect.left >= WIDTH:  # saiu pela direita
            self.rect.right = 0
        
        
        
        
        '''
        
        if self.rect.right <= 0 :
            self.rect.left = WIDTH
        
        teclas = pygame.key.get_pressed()
                                          
        if teclas[pygame.K_RIGHT]:                 
            self.rect.centerx -= 4 #SPEED[self.name]
                
        if teclas[pygame.K_LEFT]:# and self.rect.left<0:
            self.rect.centerx += 4 #SPEED[self.name]
                
                #self.rect.centerx += SPEED[self.name]
       
        '''
                
            
            
            