import game

class TestGame(Game):
    def __init__(self):
        super(TestGame, self).__init__()

    def render(self):
        pass

if __name__ == "__main__":
    game = TestGame()
    game.start()
