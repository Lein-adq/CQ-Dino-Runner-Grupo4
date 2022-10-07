import pygame
from pygame.sprite import (Sprite)
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, JUMP_SOUND


class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.dino_run_img = RUNNING
        self.dino_jump_img = JUMPING
        self.dino_duck_img = DUCKING

        self.image = self.dino_run_img[0]
        self.dino_rect = self.image.get_rect()
        self.jump_vel = self.JUMP_VEL
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.dino_step = 0
        self.jump_sound = JUMP_SOUND

    def update(self, userInput):
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False
            self.jump_sound.play()
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_jump = False
            self.dino_run = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False

        if self.dino_step >= 10:
            self.dino_step = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        self.image = RUNNING[0] if self.dino_step < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.dino_step += 1

    def jump(self):
        self.image = self.dino_jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def duck(self):
        self.image = DUCKING[0] if self.dino_step < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.dino_step += 1
