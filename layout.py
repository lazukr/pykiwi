from pos import Pos

class Layout(object):
    def __init__(self, size, pos=Pos(0,0), border=1):
        self.size = size
        self.pos = pos
        self.origin = Pos(0, 0)
        self.children = []
        self.border = border

    def _render_children(self, surface):
        for child in self.children:
            child.render(surface)

    def add(self, child):
        raise NotImplementedError

    def render(self, surface):
        raise NotImplementedError
