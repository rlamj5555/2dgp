import random
import json
from pico2d import *


image = None




class Background:
    def __init__(self):
        self.image = load_image('white_bg.png')
        self.bgm = load_music('composing for python.mp3')
        self.bgm.set_volume(60)
        self.bgm.repeat_play()


    def draw(self):
        self.image.draw(400, 300)

    def get_bb(self):
        return (0,0,800,10)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def __del__(self):
        del self.image
        del self.bgm


