import random

from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('white_bg.png')

    def draw(self):
        self.image.draw(400, 300)

    def get_bb(self):
        return (0,0,800,10)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    # fill here

