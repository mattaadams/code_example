from shapes.circle import Circle
import pygame


class Player(Circle):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 10
        elif keys[pygame.K_RIGHT]:
            self.x += 10
        elif keys[pygame.K_DOWN]:
            self.y += 10
        elif keys[pygame.K_UP]:
            self.y -= 10
