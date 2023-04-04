from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
import random



class Cactus(Obstacle):
    Y_POS_CACTUS = 320

    def __init__(self):
        self.type = random.randint(0, 2)
        self.choice = random.randint(0, 1)
        if self.choice == 0:
            image = SMALL_CACTUS[self.type]
        elif self.choice == 1:
            image = LARGE_CACTUS[self.type]
            self.Y_POS_CACTUS = 295
        super().__init__(image)
        self.rect.y = self.Y_POS_CACTUS
