import pygame
from dino_runner.utils.constants import (RUNNING, RUNNING_SHIELD, DUCKING, DUCKING_SHIELD, 
                                         JUMPING, JUMPING_SHIELD, DEFAULT_TYPE, SHIELD_TYPE, 
                                         RUNNING_HAMMER, DUCKING_HAMMER, JUMPING_HAMMER, HAMMER_TYPE,
                                         DIVING, DIVING_HAMMER, DIVING_SHIELD, DEAD)

class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5
    SUPERJUMP_VEL = 11.5
    DIVE_VEL = 8.5
    FLY_VEL = 2.5

    def __init__(self):
        self.run_img = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}
        self.duck_img = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
        self.jump_img = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
        self.dive_img = {DEFAULT_TYPE: DIVING, SHIELD_TYPE: DIVING_SHIELD, HAMMER_TYPE: DIVING_HAMMER}
        self.type = DEFAULT_TYPE
        self.image = self.run_img[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.dino_dive = False
        self.dino_superjump = False
        self.dino_fly = False
        self.jump_vel = self.JUMP_VEL
        self.superjump_vel = self.SUPERJUMP_VEL
        self.dive_vel = self.DIVE_VEL
        self.fly_vel = self.FLY_VEL
        self.dino_dead = False
        self.check_dead = False
        self.jump_sfx = pygame.mixer.Sound("dino_runner/assets/Sounds/jump_sound.wav")
        self.jump_sfx.set_volume(0.5)
        self.dive_sfx = pygame.mixer.Sound("dino_runner/assets/Sounds/dive_sound2.wav")
        self.dive_sfx.set_volume(0.5)
        self.shield = False
        self.hammer = False
        self.time_up_power_up = 0
        self.jump_sound = False
        self.dive_sound = False

    def update(self, user_input):
        if self.dino_jump:
            self.jump()
            if not self.jump_sound:
                self.jump_sfx.play()
                self.jump_sound = True
        if self.dino_superjump:
            self.superjump()
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
            self.jump_sound = False
            self.dive_sound = False
        if self.dino_dive:
            self.dive()
            if not self.dive_sound:
                self.dive_sfx.play()
                self.dive_sound = True
        if self.dino_fly:
            self.fly()

        if user_input[pygame.K_DOWN] and not self.dino_jump and not self.dino_dive:
           self.dino_run = False
           self.dino_duck = True
           self.dino_jump = False
           self.dino_dive = False
           self.dino_superjump = False
           self.dino_fly = False
        elif user_input[pygame.K_UP] and not self.dino_jump and not self.dino_superjump and not self.dino_fly and not self.dino_dive:
           self.dino_run = False
           self.dino_duck = False
           self.dino_jump = True
           self.dino_dive = False
           self.dino_superjump = False
           self.dino_fly = False
        elif user_input[pygame.K_SPACE] and not self.dino_jump and not self.dino_superjump:
           self.dino_run = False
           self.dino_duck = False
           self.dino_jump = False
           self.dino_dive = False
           self.dino_superjump = True
           self.dino_fly = False
        elif user_input[pygame.K_DOWN] and self.dino_jump and not self.dino_fly:
           self.dino_run = False
           self.dino_duck = False
           self.dino_jump = False
           self.dino_dive = True
           self.dino_superjump = False
           self.dino_fly = False
        elif user_input[pygame.K_f] and self.dino_jump and not self.dino_fly and not self.dino_dive:
           self.dino_run = False
           self.dino_duck = False
           self.dino_jump = False
           self.dino_dive = False
           self.dino_superjump = False
           self.dino_fly = True
        elif not self.dino_jump and not self.dino_superjump and not self.dino_dive and not self.dino_fly:
           self.dino_run = True
           self.dino_duck = False
           self.dino_jump = False
           self.dino_dive = False
           self.dino_superjump = False
           self.dino_fly = False
        if self.step_index >= 10:
            self.step_index = 0

        if self.shield:
            time_to_show = round((self.time_up_power_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show < 0:
                self.reset()

        if self.hammer:
            time_to_show = round((self.time_up_power_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show < 0:
                self.reset()

    def draw(self, screen):
        screen.blit(self.image, self.dino_rect)

    def run(self):
        self.image = self.run_img[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def duck(self):
        self.image = self.duck_img[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def set_power_up(self,power_up):
        if power_up.type == SHIELD_TYPE:
           self.type = SHIELD_TYPE
           self.shield = True
           self.time_up_power_up = power_up.time_up

        elif power_up.type == HAMMER_TYPE:
           self.type = HAMMER_TYPE
           self.hammer = True
           self.time_up_power_up = power_up.time_up

    def reset(self):
        self.type = DEFAULT_TYPE
        self.shield = False
        self.hammer = False
        self.time_up_power_up = 0

    def superjump(self):
        self.image = self.jump_img[self.type]
        if self.dino_superjump:
            self.dino_rect.y -= self.superjump_vel * 4
            self.superjump_vel -= 0.8
        if self.superjump_vel < -self.SUPERJUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_superjump = False
            self.superjump_vel = self.SUPERJUMP_VEL

    def dive(self):
        self.image = self.dive_img[self.type]
        self.jump_vel = self.JUMP_VEL
        self.superjump_vel = self.SUPERJUMP_VEL
        if self.dino_dive:
            self.dino_rect.y += self.dive_vel *4
            self.dive_vel += 0.8
        if self.dino_rect.y > self.Y_POS:
            self.dino_rect.y = self.Y_POS
            self.dino_dive = False
            self.dive_vel = self.DIVE_VEL
            
    def fly(self):
        self.image = self.duck_img[self.type][self.step_index // 5]
        self.jump_vel = self.JUMP_VEL
        self.superjump_vel = self.SUPERJUMP_VEL
        if self.dino_fly:
            self.dino_rect.y += self.fly_vel *2
            self.fly_vel += 0.2
        if self.dino_rect.y > self.Y_POS:
            self.dino_rect.y = self.Y_POS
            self.dino_fly = False
            self.fly_vel = self.FLY_VEL