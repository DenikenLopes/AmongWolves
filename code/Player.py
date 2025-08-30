from code.Entity import Entity
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
        

        
        
    def move(self, ):
        
        keys = pygame.key.get_pressed()
        moved = False

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= 5
            self.direction = "left"
            self.last_key = "left"
            moved = True
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += 5
            self.direction = "right"
            self.last_key = "right"
            moved = True
        
        

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