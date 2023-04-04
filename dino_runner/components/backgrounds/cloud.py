from dino_runner.components.backgrounds.background import Background
from dino_runner.utils.constants import CLOUD
import random



class Cloud(Background):

    def __init__(self):
        image = CLOUD
        super().__init__(image)
        self.rect.y = random.randint(10, 200)
