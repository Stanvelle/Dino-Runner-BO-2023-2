from dino_runner.utils.constants import SCREEN_WIDTH
import random

class Background:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(0, 2200)

    def update(self, game_speed):
        self.rect.x -= game_speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)