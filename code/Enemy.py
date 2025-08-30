from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name, position):
        super().__init__("Enemy/Enemy0", position)
    
    def move(self):
        return super().move()
    