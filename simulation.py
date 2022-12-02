import pygame
import sys

class Simulation:

    background_color = (255, 213, 128)

    def __init__(
                self,
                screen_width: int,
                screen_height: int,
                gravity:float, 
                shapes: list = []
                ):
        pygame.init()
        pygame.display.set_caption('Environment')
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.gravity = gravity
        self.shapes = shapes

    def run(self):
        while self.running:
            self.clock.tick(30)
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self._check_boundaries()
        for shape in self.shapes:
            shape.move()
            shape.fall(self.gravity)


    def _update_screen(self):
        self.screen.fill(self.background_color)
        self._draw_shapes()
        pygame.display.update()


    def _get_shape_positions(self):
        for shape in self.shapes:
            x,y = shape.x, shape.y
            

    def _check_boundaries(self):
        for shape in self.shapes:
            
            if shape.y < 20:
                shape.y_vel = 0
            if shape.y > (self.screen_height - 20):
                shape.y_vel = 0
                shape.is_falling = False

            if shape.x < 20:
                shape.x_vel = 0
            if shape.x > (self.screen_width - 20):
                shape.x_vel = 0


    def _draw_shapes(self):
        """Creates a drawing of the shape object(s) on the game screen
        """
        for shape in self.shapes:
            if shape.shape == "Rectangle":
                pygame.draw.rect(self.screen, shape.color, (shape.x, shape.y, shape.width, shape.height))
            elif shape.shape == "Circle":
                pygame.draw.circle(self.screen, shape.color,(shape.x,shape.y),shape.radius)


    @classmethod
    def set_background_color(cls,color):
        cls.background_color = color
        

