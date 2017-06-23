class Layout(object):
    def __init__(self, size, pos=(0,0)):
        self.size = size
        self.pos = pos
        self.children = []

    def add(self, child):
        self.children.append(child)

    def _render_children(self, surface):
        for child in self.children:
            child.render(surface)

    def render(self, surface):
        raise NotImplementedError
