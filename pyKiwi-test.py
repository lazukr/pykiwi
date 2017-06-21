from uielement import UIElement
import pygame

SCREEN_SIZE = (640, 480)

class Game:
    def __init__(self, dim=SCREEN_SIZE, fps=30, bgcolor=(255,255,255)):
        self.dim = dim
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.background_color = bgcolor
        self.layouts = []
        self.items = []

    def start(self):
        pygame.display.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(self.dim)
        self.render()
        is_running = True

        while is_running:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                self.render()

            pygame.display.flip()
        pygame.quit()

    def render(self):
        self.screen.fill(self.background_color)
        self._ItemRender()
        self._LayoutRender()


    def AddLayout(self, layout):
        self.layouts.append(layout)

    def AddItem(self, item):
        self.items.append(item)

    def _ItemRender(self):
        for item in self.items:
            item.update()

    def _LayoutRender(self):
        for layout in self.layouts:
            layout.update(self.screen)



if __name__ == "__main__":
    game = Game()
    ui = UIElement(dim=(50, 50), background_color=(100, 100, 100))
    game.AddLayout(ui)
    game.start()