import pygame.image
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    
    def __init__(self, window):
        self.window = window        
        self.entity_list: list[Entity] = []  #adiciona em uma lista as entidades: inimigos, cenário, personagem
        self.entity_list.extend(EntityFactory.get_entity('back'))
        self.entity_list.extend(EntityFactory.get_entity('Enemy'))
        self.entity_list.extend(EntityFactory.get_entity('p'))
        
                
    def run(self):
        clock = pygame.time.Clock()    
        while True:
            clock.tick(60)
            
            teclas = pygame.key.get_pressed()
            direction = 0
            if teclas[pygame.K_RIGHT]:
                direction = 1
            elif teclas[pygame.K_LEFT]:
                direction = -1
            
            for ent in self.entity_list:
            
                self.window.blit(source=ent.surf, dest=ent.rect)
                
                # só background recebe direction
                from code.Background import Background
                from code.Enemy import Enemy
                if isinstance(ent, Background):
                    ent.move(direction)
                elif isinstance(ent, Enemy):
                    ent.move(direction)
                else:
                    ent.move()
                
                
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            pygame.display.flip()
            
            '''
             # salvando todas as camadas do cenário em uma lista
        self.camada = []
        self.camada.append(pygame.image.load('./asset/back0.png'))
        self.camada.append(pygame.image.load('./asset/back1.png'))
        self.camada.append(pygame.image.load('./asset/back2.png'))
        self.camada.append(pygame.image.load('./asset/back3.png'))
        self.camada.append(pygame.image.load('./asset/back4.png'))
        self.camada.append(pygame.image.load('./asset/back5.png'))
            
            
            
            #código paralax         
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
                            
            '''
           
