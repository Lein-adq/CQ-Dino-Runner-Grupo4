import pygame
import random
from dino_runner.components.obstacles.cactus import LargeCactus, SmallCactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import (
    LARGE_CACTUS,
    SMALL_CACTUS,
    BIRD
)


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle_app = random.randint(1, 3)
            if obstacle_app == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif obstacle_app == 2:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif obstacle_app == 3:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed)

            if obstacle.image_rect.x < -obstacle.image_rect.width:
                self.obstacles.pop()

            if game.dino.dino_rect.colliderect(obstacle.image_rect):
                pygame.time.delay(500)
                game.death_count += 1
                self.obstacles.pop()

                if game.death_count == 5:
                    game.playing = False
                    game.execute()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

