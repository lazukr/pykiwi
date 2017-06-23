from game import Game

from listlayout import ListLayout
from button import Button

class TestGame(Game):
    def __init__(self):
        super(TestGame, self).__init__()

    def setup(self):
        layout = ListLayout((150, 300))
        for i in xrange(4):
            button = Button('Click Me')
            layout.add(button)
        return layout

    def render(self):
        pass


if __name__ == "__main__":
    game = TestGame()
    game.start()
