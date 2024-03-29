import pygame
from pygame.sprite import (Sprite)
from utils.constants import RUNNING, JUMPING, DUCKING, JUMP_SOUND


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
        self.dino_stop_jump = False
        self.dino_duck = False
        self.dino_step = 0
        self.jump_sound = JUMP_SOUND

    def update(self, user_input):
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()
        if self.dino_stop_jump:
            self.stop_jump()

        if (user_input[pygame.K_UP] or user_input[pygame.K_SPACE]) and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False
            self.dino_stop_jump = False
            self.jump_sound.play()
            self.jump_sound.set_volume(0.60)

        elif user_input[pygame.K_DOWN] and self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = False
            self.dino_stop_jump = True

        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_jump = False
            self.dino_run = False
            self.dino_stop_jump = False

        elif not (self.dino_jump or user_input[pygame.K_DOWN]):
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False
            self.dino_stop_jump = False

        if self.dino_step >= 10:
            self.dino_step = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def draw_dinosaur(self, image_list, dino_pos_y):
        self.image = image_list[0] if self.dino_step < 5 else image_list[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = dino_pos_y
        self.dino_step += 1

    def run(self):
        self.draw_dinosaur(RUNNING, self.Y_POS)

    def duck(self):
        self.draw_dinosaur(DUCKING, self.Y_POS_DUCK)

    def jump(self):
        self.image = self.dino_jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def stop_jump(self):
        if self.jump_vel < self.JUMP_VEL:
            self.dino_rect.y += self.jump_vel * 4
            self.jump_vel += 0.8
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL
