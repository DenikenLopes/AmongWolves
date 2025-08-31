from code.Background import Background
from code.Player import Player
from code.Enemy import Enemy
from code.Const import WIDTH
import pygame


class EntityFactory:
    
    @staticmethod      
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'back':
                listBack = []
                for i in range(6):
                    listBack.append(Background(f'back{i}', (0,0)))
                    listBack.append(Background(f'back{i}', (WIDTH-1,0)))
                return listBack
            
            case 'p':
                position = (40, 350)
                sprites = {
                    "left":  [pygame.image.load(f"./asset/player/left/p{i}.png").convert_alpha() for i in range(3)],
                    "right": [pygame.image.load(f"./asset/player/right/p{i}.png").convert_alpha() for i in range(3)],
                    "stop": [pygame.image.load(f"./asset/player/p{i}.png").convert_alpha() for i in range(2)],
                }
                rect = sprites["right"][0].get_rect(center=position)
                return [Player(sprites["right"][0], rect, sprites)]
            
            case 'Enemy':
                position = (WIDTH-200, 275)
                sprites = {
                    "walk": [pygame.image.load(f"./asset/enemy/Enemy{i}.png").convert_alpha() for i in range(5)],
                    #"stop": [pygame.image.load("./asset/enemy/enemy_stop.png").convert_alpha()],
                }
                return [Enemy('enemy0', position, sprites)]