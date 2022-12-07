from shapes.circle import Circle
import pygame


class Player(Circle):
    """
    A player which is derived from the Circle class.
    The player class shares the same parameters of the circle,
    but is able to move freely by using the arrow keys.

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def move(self):
        """Overrides the original method to allow
           for the user to controlobjects movement with
           their computer keyboard."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 10
        elif keys[pygame.K_RIGHT]:
            self.x += 10
        elif keys[pygame.K_DOWN]:
            self.y += 10
        elif keys[pygame.K_UP]:
            self.y -= 10
