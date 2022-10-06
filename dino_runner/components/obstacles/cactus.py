from dino_runner.components.obstacles.obstacle import Obstacle
import random


class LargeCactus(Obstacle):
    def __init__(self, image, pos=300):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.image_rect.y = pos


class SmallCactus(Obstacle):
    def __init__(self, image, pos=325):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.image_rect.y = pos
