import random
from pygame.sprite import Sprite
from utils.constants import CLOUD, SCREEN_WIDTH


class Cloud(Sprite):
    def __init__(self):
        self.cloud_img = CLOUD
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = self.cloud_img
        self.width = self.image.get_width()

    def update(self, game):
        self.x -= game.game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
