import pygame

from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

BLACK_COLOR = (0, 0, 0)
FONT_STYLE1 = "freesansbold.ttf"
FONT_STYLE2 = "assets/fonts/pixelfont.ttf"


def get_score_element(points, font=FONT_STYLE1):
    font = pygame.font.Font(font, 22)
    text = font.render("Points : " + str(points), True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (980, 40)
    return text, text_rect

    # self.screen.blit(text, textRect)


def get_centered_message(message, width=(SCREEN_WIDTH // 2), height=(SCREEN_HEIGHT // 2), font_size=22, font=FONT_STYLE2):
    font = pygame.font.Font(font, font_size)
    text = font.render(message, True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect
