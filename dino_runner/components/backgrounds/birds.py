from dino_runner.components.backgrounds.background import Background
from dino_runner.utils.constants import BIRD
import random



class Birds(Background):

    def __init__(self):
        self.type = random.randint(0, 1)
        image = BIRD[self.type]
        super().__init__(image)
        self.rect.y = random.randint(10, 200)
