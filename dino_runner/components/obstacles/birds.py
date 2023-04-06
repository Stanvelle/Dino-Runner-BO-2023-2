from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
from dino_runner.utils.constants import BLUE_BIRD
from dino_runner.utils.constants import RED_BIRD
from dino_runner.utils.constants import YELLOW_BIRD
from dino_runner.utils.constants import ORANGE_BIRD
from dino_runner.utils.constants import SCREEN_WIDTH
import random

class Birds(Obstacle):

    def __init__(self):
        self.type = random.randint(0, 1)
        self.choice = random.randint(0, 4)
        if self.choice == 0:
            image = BIRD[self.type]
        elif self.choice == 1:
            image = BLUE_BIRD[self.type]
        elif self.choice == 2:
            image = RED_BIRD[self.type]
        elif self.choice == 3:
            image = YELLOW_BIRD[self.type]
        elif self.choice == 4:
            image = ORANGE_BIRD[self.type]
        super().__init__(image)
        self.rect.y = random.randint(0, 270)
        self.step_index = 0
        self.rect.x = SCREEN_WIDTH + random.randint(0, 2200)

    def update(self,game_speed,player):
        if self.choice == 0:
            self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
            self.step_index += 1
            if self.step_index >= 10:
                self.step_index = 0
        elif self.choice == 1:
            self.image = BLUE_BIRD[0] if self.step_index < 5 else BLUE_BIRD[1]
            self.step_index += 1
            if self.step_index >= 10:
                self.step_index = 0
        elif self.choice == 2:
            self.image = RED_BIRD[0] if self.step_index < 5 else RED_BIRD[1]
            self.step_index += 1
            if self.step_index >= 10:
                self.step_index = 0
        elif self.choice == 3:
            self.image = YELLOW_BIRD[0] if self.step_index < 5 else YELLOW_BIRD[1]
            self.step_index += 1
            if self.step_index >= 10:
                self.step_index = 0
        elif self.choice == 4:
            self.image = ORANGE_BIRD[0] if self.step_index < 5 else ORANGE_BIRD[1]
            self.step_index += 1
            if self.step_index >= 10:
                self.step_index = 0
        return super().update(game_speed,player)

