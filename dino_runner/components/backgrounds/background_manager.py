from dino_runner.components.backgrounds.birds import Birds
from dino_runner.components.backgrounds.cloud import Cloud


class BackgroundManager:
    def __init__(self):
        self.birds = []
        self.cloud = []
        self.cloud2 = []

    def update(self, game_speed):
        if len(self.birds) == 0:
            self.birds.append(Birds())
        if len(self.cloud) == 0:
            self.cloud.append(Cloud())
        if len(self.cloud2) == 0:
            self.cloud2.append(Cloud())
        for bird in self.birds:
            if bird.rect.x < -bird.rect.width:
                self.birds.pop()
            bird.update(game_speed)
        for cloud in self.cloud:
            if cloud.rect.x < -cloud.rect.width:
                self.cloud.pop()
            cloud.update(game_speed)
        for cloud in self.cloud2:
            if cloud.rect.x < -cloud.rect.width:
                self.cloud2.pop()
            cloud.update(game_speed)

    def draw(self, screen):
        for bird in self.birds:
            bird.draw(screen)
        for cloud in self.cloud:
            cloud.draw(screen)
        for cloud in self.cloud2:
            cloud.draw(screen)