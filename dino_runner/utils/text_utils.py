import pygame

from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

BLACK_COLOR = (0, 0, 0)
FONT_STYLE1 = "freesansbold.ttf"
FONT_STYLE2 = "assets/fonts/pixelfont.ttf"
FONT_STYLE3 = "assets/fonts/DTM-SANS.otf"
FONT_STYLE4 = "assets/fonts/DTM-MONO.otf"


def get_score_element(points, widths=(SCREEN_WIDTH - 120), heights=(SCREEN_HEIGHT - 560), font=FONT_STYLE3):
    font = pygame.font.Font(font, 22)
    text = font.render("Points : " + str(points), True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (widths, heights)
    return text, text_rect

    # self.screen.blit(text, textRect)


def get_centered_message(message, width=(SCREEN_WIDTH // 2), height=(SCREEN_HEIGHT // 2), font_size=22, font=FONT_STYLE4):
    font = pygame.font.Font(font, font_size)
    text = font.render(message, True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect
