from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.birds import Birds
import pygame

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.obstacles2 = []
        self.sfx = pygame.mixer.Sound("dino_runner/assets/Sounds/hit.wav")

    def update(self, game_speed, player):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus())
        if len(self.obstacles2) == 0:
            self.obstacles2.append(Birds())
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.pop()
            if obstacle.rect.colliderect(player.dino_rect) and player.hammer:
                self.obstacles.pop()
                self.sfx.play()
            obstacle.update(game_speed,player)
        for obstacle in self.obstacles2:
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles2.pop()
            if obstacle.rect.colliderect(player.dino_rect) and player.hammer:
                self.obstacles2.pop()
                self.sfx.play()
            obstacle.update(game_speed,player)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        for obstacle in self.obstacles2:
            obstacle.draw(screen)