from game import Game
from listlayout import ListLayout
from button import Button
from size import Size
from pos import Pos
from text import Text

import styles
import orientation
import colour
import events
import pygame

def on_button_click():
    print 'button clicked'

class TestGame(Game):
    def __init__(self):
        super(TestGame, self).__init__()
        self.view = []

    def render_root(self):
        self.view.append(
            ListLayout(Size(150, 300), Pos(100,100), 5, 2, orientation.HORIZONTAL, styles.FIT)
            )
        for i in xrange(6):
            button = Button('Click Me')
            button.attach_hover(
                Text(Size(50, 20), str(i), 20)
            )
            self.on(button, events.CLICK, on_button_click)
            self.on(button, events.HOVER)
            self.view[0].add(button)

        return self.view

    def render(self):
        pass


if __name__ == "__main__":
    game = TestGame()
    game.start()
