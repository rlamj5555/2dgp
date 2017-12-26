from pico2d import *


class Ground:
    def __init__(self):
        pass

    def draw(self):
        pass

    def get_bb(self):
        return 0, 0, 800, 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())