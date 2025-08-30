from code.Background import Background
from code.Const import WIDTH
import pygame


class EntityFactory:
    
    @staticmethod      
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'back':
                listBack = []
                for i in range(6):
                    listBack.append(Background(f'back{i}', (0,0))) #coloca todos o nomes dos background em uma lista
                    listBack.append(Background(f'back{i}', (WIDTH,0)))
                return listBack
            
            case 'player':
                pass
                    