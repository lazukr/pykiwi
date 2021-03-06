from game import Game
from listlayout import ListLayout
from button import Button
from size import Size
from pos import Pos

import styles
import orientation
import colour
import events

def on_button_click():
    print 'button clicked'

class TestGame(Game):
    def __init__(self):
        super(TestGame, self).__init__()

    def render_root(self):
        layout = ListLayout(Size(150, 300), Pos(100,100), 5, 2, orientation.HORIZONTAL, styles.FIT)
        for i in xrange(6):
            button = Button('Click Me')
            self.on(button, events.CLICK, on_button_click) 
            layout.add(button)

        return layout

    def render(self):
        pass


if __name__ == "__main__":
    game = TestGame()
    game.start()
