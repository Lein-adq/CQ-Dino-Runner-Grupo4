import pygame
import random
from components.obstacles.cactus import LargeCactus, SmallCactus
from components.obstacles.bird import Bird
from utils.constants import (
    LARGE_CACTUS,
    SMALL_CACTUS,
    BIRD, HURT_SOUND, DEATH_SOUND
)


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.coll_sound = HURT_SOUND
        self.death_sound = DEATH_SOUND

    def update(self, game):
        bird = Bird(BIRD, random.choice([200, 250, 300]))
        if len(self.obstacles) == 0:
            obstacle_app = random.randint(1, 3)
            if obstacle_app == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif obstacle_app == 2:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif obstacle_app == 3:
                self.obstacles.append(bird)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed)

            if obstacle.image_rect.x < -obstacle.image_rect.width:
                self.obstacles.pop()

            if game.dino.dino_rect.colliderect(obstacle.image_rect):
                pygame.time.delay(300)
                game.death_count += 1
                self.obstacles.pop()
                self.coll_sound.play(2)
                self.coll_sound.set_volume(0.18)
                if game.death_count == 5:
                    pygame.time.delay(500)
                    pygame.mixer.Sound.play(self.death_sound)
                    pygame.mixer.Sound.set_volume(self.death_sound, 0.45)
                    game.playing = False
                    game.execute()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
