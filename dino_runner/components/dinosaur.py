from pygame.sprite import (Sprite)
from utils.constants import RUNNING


class Dinosaur(Sprite):
    X_POS = 50
    Y_POS = 300

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.dino_run = True
        self.dino_step = 0

    def update(self):
        self.run()
        if self.dino_step >= 10:
            self.dino_step = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        self.image = RUNNING[0] if self.dino_step < 5 else RUNNING[1]
        print(self.dino_step)
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.dino_step += 1
