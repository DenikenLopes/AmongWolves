from code.Entity import Entity
from code.Const import WIDTH, SPEED
import pygame


class Background(Entity):
    
    def __init__(self, name, position):
        super().__init__(name, position)
    
    def move(self, ):
        
        teclas = pygame.key.get_pressed()
                                  
        if teclas[pygame.K_RIGHT]:
                self.rect.centerx -= SPEED[self.name]
        if teclas[pygame.K_LEFT]:
                self.rect.centerx += SPEED[self.name]
        
        if self.rect.right <= 0:
            self.rect.left = WIDTH           
            
            
            