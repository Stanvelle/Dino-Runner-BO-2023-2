from dino_runner.components.backgrounds.birds import Birds
from dino_runner.components.backgrounds.cloud import Cloud


class BackgroundManager:
    def __init__(self):
        self.birds = []
        self.cloud = []
        self.cloud2 = []
        self.cloud3 = []
        self.cloud4 = []
        self.cloud5 = []
        #Pendiente volver esto un diccionario de listas.

    def update(self, game_speed, player):
        if len(self.birds) == 0:
            self.birds.append(Birds())
        if len(self.cloud) == 0:
            self.cloud.append(Cloud())
        #if len(self.cloud2) == 0:
        #    self.cloud2.append(Cloud())
        #if len(self.cloud3) == 0:
        #    self.cloud3.append(Cloud())
        #if len(self.cloud4) == 0:
        #    self.cloud4.append(Cloud())
        #if len(self.cloud5) == 0:
        #    self.cloud5.append(Cloud())
        for bird in self.birds:
            if bird.rect.x < -bird.rect.width:
                self.birds.pop()
            bird.update(game_speed, player)
        for cloud in self.cloud:
            if cloud.rect.x < -cloud.rect.width:
                self.cloud.pop()
            cloud.update(game_speed)
        #for cloud in self.cloud2:
        #    if cloud.rect.x < -cloud.rect.width:
        #        self.cloud2.pop()
        #    cloud.update(game_speed, player)
        #for cloud in self.cloud3:
        #    if cloud.rect.x < -cloud.rect.width:
        #        self.cloud3.pop()
        #    cloud.update(game_speed, player)
        #for cloud in self.cloud4:
        #    if cloud.rect.x < -cloud.rect.width:
        #        self.cloud4.pop()
        #    cloud.update(game_speed, player)
        #for cloud in self.cloud5:
        #    if cloud.rect.x < -cloud.rect.width:
        #        self.cloud5.pop()
        #    cloud.update(game_speed, player)

    def draw(self, screen):
        for bird in self.birds:
            bird.draw(screen)
        for cloud in self.cloud:
            cloud.draw(screen)
        #for cloud in self.cloud2:
        #    cloud.draw(screen)
        #for cloud in self.cloud3:
        #    cloud.draw(screen)
        #for cloud in self.cloud4:
        #    cloud.draw(screen)
        #for cloud in self.cloud5:
        #    cloud.draw(screen)