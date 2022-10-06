import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import (
    LARGE_CACTUS,
    SMALL_CACTUS
)


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(LARGE_CACTUS))
        for obstacle in self.obstacles:
            obstacle.update(self)

            if obstacle.image_rect.x < -obstacle.image_rect.width:
                self.obstacles.pop()
            if game.dino.dino_rect.colliderect(obstacle.image_rect):
                pygame.time.delay(500)
                game.death_count += 1
                self.obstacles.pop()
                if game.death_count == 5:
                    game.playing = False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

