from code.Entity import Entity
from code.Const import COR_WHITE, WIDTH
import pygame

class Player(Entity):
    
    def __init__(self, name, position, sprites=None):
        super().__init__("player/right/p0", position)
        self.surf = pygame.transform.scale(self.surf, (93-10, 184-10))
        self.sprites = sprites       # dicionário { "left": [...], "right": [...] }
        self.direction = "right"
        self.frame = 0
        self.animation_speed = 0.20
        self.position = (40, 250)
        self.last_key = "right"
        #self.font = pygame.font.Font('./fonte/chinese_rocks_rg.otf', 32)
        

        
        
    def move(self, ):
        
        keys = pygame.key.get_pressed()
        moved = False

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.rect.x == 4:
                self.rect.x = 4
            else:
                self.rect.x -= 5
            
            self.direction = "left"
            self.last_key = "left"
            #print('left: ', self.rect.x)
            moved = True
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.rect.x == 649:
                self.rect.x = 649
            else:
                self.rect.x += 5
            
            self.direction = "right"
            self.last_key = "right"
            #print('right: ', self.rect.x)
            moved = True
        elif keys[pygame.K_UP]:
            if self.rect.y == 218:
                self.rect.y = 218 
            else:
                self.rect.y -= 5
            moved = True
        
        elif keys[pygame.K_DOWN]:
            if self.rect.y == 298:
                self.rect.y = 298 
            else:
                self.rect.y += 5
            moved = True
        
        #position = (40, 350)
        

        # animação
        if moved and self.sprites:
            frames = self.sprites[self.direction]
            self.frame += self.animation_speed
            if self.frame >= len(frames):
                self.frame = 0
            self.surf = frames[int(self.frame)]
        else:
            self.direction = "stop"
            if self.last_key == "left":
                #if self.sprites:
                    self.surf = self.sprites[self.direction][1]
            elif self.last_key == "right":
                self.surf = self.sprites[self.direction][0]
                
            # parado → primeiro frame da direção
            
                    
        
        #teclas = pygame.key.get_pressed()
        
        
        '''                          
        if teclas[pygame.K_RIGHT]:
                    self.rect.centerx += 3
                    #self.surf.subsurface = int(2)
                    #self.window.blit(source=listPlayer.surf, dest=listPlayer.rect)
                    
                                 
        if teclas[pygame.K_LEFT]:
                    self.rect.centerx -= 3
        '''