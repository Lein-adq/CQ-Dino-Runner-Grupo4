from components.addittional_features.feature import Feature
from utils.constants import HAMMER, SCREEN_WIDTH


class Hammer(Feature):
    def __init__(self, image):
        super().__init__(image)
        self.image_rect.y = 345


