import pygame

from components.dinosaur import Dinosaur
from components.not_interactable.cloud import Cloud
from components.obstacles.obstacle_manager import ObstacleManager
from utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, RUNNING
from utils import text_utils


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_running = True
        self.dino = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.cloud = Cloud()
        self.game_speed = 15
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.death_count = 0
        self.points = 0
        self.music = 0

    def run(self):
        # Game loop: events - update - draw
        self.reset_attributes()
        self.play_music()
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.score()
        pygame.quit()

    def reset_attributes(self):
        self.playing = True
        self.death_count = 0
        self.music = 1
        self.points = 0
        self.game_speed = 15

    def execute(self):
        self.play_music()
        while self.game_running:
            if not self.playing:
                self.show_menu()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.dino.update(user_input)
        self.obstacle_manager.update(self)
        self.cloud.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.score()
        self.lives_remain()
        self.dino.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.cloud.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        text, text_rect = text_utils.get_score_element(self.points)
        self.screen.blit(text, text_rect)

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):

        self.screen.fill((255, 255, 255))
        self.show_menu_options()

        pygame.display.update()

        self.handle_events_menu()

    def handle_events_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.run()
            if event.type == pygame.QUIT:
                self.game_running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()

    def show_menu_options(self):
        message = "WELCOME TO DINO RUNNER GAME!!" if self.death_count <= 0 else "GAME OVER"
        text, text_rect = text_utils.get_centered_message(message, font_size=30)
        self.screen.blit(text, text_rect)
        pos_y = (SCREEN_HEIGHT // 2) + 30

        game_over_message = "Press any key to start"
        text_instruction, text_instruction_rect = text_utils.get_centered_message(game_over_message, height=pos_y)

        self.screen.blit(text_instruction, text_instruction_rect)

        self.screen.blit(RUNNING[0], (((SCREEN_WIDTH // 2) - 45), pos_y - 150))

    def lives_remain(self):
        die_message = "5 DIES = GAME OVER"
        die_inst, die_inst_rect = text_utils.get_centered_message(die_message, 174, 40)
        self.screen.blit(die_inst, die_inst_rect)

        show_dies = "DIES : "
        die_inst_2, die_inst_rect_2 = text_utils.get_centered_message((show_dies + str(self.death_count)), 100, 80)
        self.screen.blit(die_inst_2, die_inst_rect_2)

    def play_music(self):
        if self.music == 0:
            pygame.mixer.music.load("assets/sounds/OST-23.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.25)
        elif self.music == 1:
            pygame.mixer.music.load("assets/sounds/01-Running-About.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.7)
            if self.death_count == 5:
                pygame.mixer.music.stop()
