from pygame.sprite import (Sprite)
from utils.constants import SCREEN_WIDTH


class Feature(Sprite):

    def __init__(self, image):
        self.image = image
        self.image_rect = self.image.get_rect()
        self.image_rect.x = SCREEN_WIDTH

    def update(self, game):
        self.image_rect.x -= game

    def draw(self, screen):
        screen.blit(self.image, self.image_rect)
