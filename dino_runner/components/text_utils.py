import pygame

from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

black_color = (0, 0, 0)
FONT_STYLE = "freesansbold.ttf"


def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE, 22)
    text = font.render("Points : " + str(points), True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (1000, 40)
    return text, text_rect
    # textRect = text.get_rect()
    # self.screen.blit(text, textRect)


def get_centered_message(message, width = (SCREEN_WIDTH / 2), height = (SCREEN_HEIGHT / 2)):
    font = pygame.font.Font(FONT_STYLE, 22)
    text = font.render(message, True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect
