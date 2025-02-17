from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
import random
import pygame

class PowerUpManager():
    def __init__(self):
        self.power_ups = []
        self.power_up_sfx = pygame.mixer.Sound("dino_runner/assets/Sounds/power_up_pick.wav")

    def update(self,game_speed,points,player):
        self.choice = random.randint(0,1)
        if self.choice == 0:
            self.select = Shield()
        else:
            self.select = Hammer()
        if len(self.power_ups) == 0 and points % 200 == 0:
            self.power_ups.append(self.select)
        for power_up in self.power_ups:
            if power_up.rect.x < -power_up.rect.width or power_up.used:
                self.power_ups.pop()
            if power_up.used:
                player.set_power_up(power_up)
                self.power_up_sfx.play()
            power_up.update(game_speed, player)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
            