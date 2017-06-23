import pygame

SCREEN_SIZE = (640, 480)

class Game(object):
    def __init__(self, dim=SCREEN_SIZE, fps=30, background_color=(255,255,255)):
        self.dim = dim
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.background_color = background_color
        self.screen = None

    def renderRoot(self, root):
        root.render(self.screen)

    def start(self):
        pygame.display.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(self.dim)
        is_running = True

        root = self.setup()
        self.renderRoot(root)

        while is_running:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                self.render()

            pygame.display.flip()
        pygame.quit()

    def render(self):
        raise NotImplementedError

    def setup(self):
        raise NotImplementedError
