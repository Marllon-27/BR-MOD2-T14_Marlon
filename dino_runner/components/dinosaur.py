import pygame

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

RUN_IMG = [RUNNING[0], RUNNING[1]]
X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5
Y_DUCK_POS = 340

class Dinosaur:
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = 0
        self.dino_rect.y = 0
        self.step_index = 0
        self.running: bool = False
        self.jump: bool = False
        self.jump_vel = JUMP_VEL
        self.ducking = False

    def update(self, user_input):

        if self.running:
             self.run()
        elif self.jump:
            self.dino_jump()
        elif self.ducking:
            self.duck()

        if user_input[pygame.K_UP] and not self.jump:
            self.running = False
            self.jump = True
        elif user_input[pygame.K_DOWN] and not self.jump:
            self.jump = False
            self.running = False 
            self.ducking = True     
        elif not self.jump and not self.ducking:
            self.jump = False
            self.running = True        

        if self.step_index >= 9:
           self.step_index = 0
    
    def run(self):
        if self.step_index < 5:
            self.image = RUN_IMG[0]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = X_POS
            self.dino_rect.y = Y_POS
        else:
            self.image = RUN_IMG[1]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = X_POS
            self.dino_rect.y = Y_POS
        
        self.step_index += 1

    def dino_jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_vel * 4
        self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            # self.dino_rect.y += self.jump_vel * 4
            # self.jump_vel += 1
            self.dino_rect.y = Y_POS
            self.jump = False
            self.jump_vel = JUMP_VEL
          
    def duck(self):
        
        if self.step_index < 5:
            self.image = DUCKING[0]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = X_POS
            self.dino_rect.y = Y_DUCK_POS
        else:
            self.image = DUCKING[1]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = X_POS
            self.dino_rect.y = Y_DUCK_POS            
        
        self.step_index += 1
        self.ducking = False        

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
