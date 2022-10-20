from components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self, image, pos):
        self.type = 0
        super().__init__(image, self.type)
        self.image_rect.y = pos
        self.fly = 0

    def draw(self, screen):
        if self.fly >= 9:
            self.fly = 0
        screen.blit(self.image[self.fly//5], self.image_rect)
        self.fly += 1
