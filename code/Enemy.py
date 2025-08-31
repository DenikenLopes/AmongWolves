from code.Entity import Entity
from code.Const import SPEED
import pygame

class Enemy(Entity):
    def __init__(self, name: str, position: tuple, sprites: dict, speed=-1):
        super().__init__("Enemy/Enemy0", position)
        
        self.sprites = sprites or {}
        if "walk" not in self.sprites:
            self.sprites["walk"] = [self.surf]
        if "stop" not in self.sprites:
            self.sprites["stop"] = [self.sprites["walk"][0]]

        # 4 frames para o pulo (últimos do walk)
        walk_frames = self.sprites["walk"]
        if len(walk_frames) >= 5:
            self.sprites["jump"] = walk_frames[-4:]
        else:
            self.sprites["jump"] = [walk_frames[-1:]]

        self.speed = speed

        # física
        self.vel_y = 0.0
        self.gravity = 0.8
        self.jump_strength = -12
        self.ground_y = position[1]
        self.is_jumping = False

        # pausa
        self.is_paused = False
        self.pause_duration = 100  # 2 segundos
        self.pause_start = 0

        # temporizador para pulo automático
        self.jump_interval_ms = 1200
        self.last_jump_ms = pygame.time.get_ticks()

        # animação
        self.direction = "walk"
        self.frame_counter = 0.0
        self.animation_speed = 0.15

        # sprite inicial
        self.surf = self.sprites["walk"][1]
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
    
    def move(self, direction):
        now = pygame.time.get_ticks()

        # Se está pausado → não anda no X e fica parado
        if self.is_paused:
            if now - self.pause_start >= self.pause_duration:
                self.is_paused = False
                self.last_jump_ms = now  # reseta contador de pulo
            else:
                # Fica completamente parado (sem X, sem Y)
                self.direction = "stop"
                self.surf = self.sprites["stop"][0]
                return

        self.rect.x += self.speed

        # inicia pulo automático
        if not self.is_jumping and (now - self.last_jump_ms) >= self.jump_interval_ms:
            self.vel_y = self.jump_strength
            self.is_jumping = True
            self.direction = "jump"
            self.last_jump_ms = now

        # gravidade
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        # checa chão
        if self.rect.y >= self.ground_y:
            self.rect.y = self.ground_y
            self.vel_y = 0
            if self.is_jumping:
                self.is_jumping = False
                self.direction = "walk"
                # ativa pausa de 2 segundos
                self.is_paused = True
                self.pause_start = now
                return  # sai antes de atualizar animação

        # animação
        frames = self.sprites[self.direction]
        self.frame_counter += self.animation_speed
        if self.frame_counter >= len(frames):
            self.frame_counter = 0.0
        self.surf = frames[int(self.frame_counter)]
        
        '''
        now = pygame.time.get_ticks()

        # depois de um tempo para
        if now - self.start_time > self.stop_time:
            self.direction = "stop"
            self.speed = 0

        # só anda se não estiver parado
        if self.direction == "walk":
            self.rect.x += self.speed

        # animação
        if now - self.animation_timer > self.frame_delay:
            self.animation_timer = now
            frames = self.sprites[self.direction]
            self.current_frame = (self.current_frame + 1) % len(frames)
            self.surf = frames[self.current_frame]
    '''