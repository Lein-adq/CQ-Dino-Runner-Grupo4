from pygame.sprite import Sprite

from dino_runner.utils.constants import HEART


class Heart(Sprite):
    def __init__(self):
        self.heart_img = HEART
        self.image = self.heart_img
        self.x = 1000
        self.y = 500

    def draw(self, screen):
        screen.blit(self.image)
