import random

from components.addittional_features.hammer import Hammer
from utils.constants import (
    HAMMER
)


class FeatureManager:
    def __init__(self):
        self.features = []
        self.possibilities = int

    def update(self, game):
        self.possibilities = random.randrange(1, 100)
        if self.possibilities == 5:
            self.features.append(Hammer(HAMMER))
            # self.possibilities = 0
        for feature in self.features:
            feature.update(game.game_speed)

            if feature.image_rect.x < -feature.image_rect.width:
                self.features.pop()

            if game.dino.dino_rect.colliderect(feature.image_rect):
                self.features.pop()

    def draw(self, screen):
        for feature in self.features:
            feature.draw(screen)
