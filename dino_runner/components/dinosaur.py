import pygame
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5
    SUPERJUMP_VEL = 8.5
    DIVE_VEL = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.dino_dive = False
        self.dino_superjump = False
        self.jump_vel = self.JUMP_VEL
        self.superjump_vel = self.SUPERJUMP_VEL
        self.dive_vel = self.DIVE_VEL

    def update(self, user_input):
        if self.dino_jump:
            self.jump()
        if self.dino_superjump:
            self.superjump()
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_dive:
            self.dive()

        if user_input[pygame.K_DOWN] and not self.dino_jump:
           self.dino_run = False
           self.dino_duck = True
           self.dino_jump = False
           self.dino_dive = False
           self.dino_superjump = False
        elif user_input[pygame.K_UP] and not self.dino_jump and not self.dino_superjump:
           self.dino_run = False
           self.dino_duck = False
           self.dino_jump = True
           self.dino_dive = False
           self.dino_superjump = False
        elif user_input[pygame.K_SPACE] and not self.dino_jump and not self.dino_superjump:
           self.dino_run = False
           self.dino_duck = False
           self.dino_jump = False
           self.dino_dive = False
           self.dino_superjump = True
        elif user_input[pygame.K_DOWN] and self.dino_jump and not self.dino_duck:
           self.dino_run = False
           self.dino_duck = False
           self.dino_jump = False
           self.dino_dive = True
           self.dino_superjump = False
        elif not self.dino_jump and not self.dino_superjump:
           self.dino_run = True
           self.dino_duck = False
           self.dino_jump = False
           self.dino_dive = False
           self.dino_superjump = False
        if self.step_index >= 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, self.dino_rect)

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def superjump(self):
        self.image = JUMPING
        if self.dino_superjump:
            self.dino_rect.y -= self.superjump_vel * 4
            self.superjump_vel -= 0.8
        if self.superjump_vel < -self.SUPERJUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_superjump = False
            self.superjump_vel = self.SUPERJUMP_VEL

    def dive(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.jump_vel = self.JUMP_VEL
        self.superjump_vel = self.SUPERJUMP_VEL
        if self.dino_dive:
            self.dino_rect.y -= self.dive_vel *4
            self.dive_vel -= 0.8
        if self.dive_vel < -self.DIVE_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_dive = False
            self.dive_vel = self.DIVE_VEL