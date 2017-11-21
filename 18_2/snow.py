import random

from pico2d import *

class Smallsnow:

    image = None;

    def __init__(self):
        self.x, self.y = random.randint(150, 750), 500
        self.fall_speed = random.randint(150, 190)
        if Smallsnow.image == None:
            Smallsnow.image = load_image('small snow.png')

    def update(self, frame_time):
         self.y -= frame_time * self.fall_speed

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
        # fill here


class Bigsnow(Smallsnow):
    image = None
    def __init__(self):
        self.x, self.y = random.randint(150, 750), 500
        self.fall_speed = random.randint(120,150)
        if Bigsnow.image == None:
            Bigsnow.image = load_image('big snow.png')

    def update(self, frame_time):
         self.y -= frame_time * self.fall_speed

    def stop(self):
        self.fall_speed = 0

    def get_bb(self):
         return self.x - 40, self.y - 40, self.x + 40, self.y + 40


class Flame(Smallsnow):
    image = None
    def __init__(self):
        self.x, self.y = random.randint(150, 750), 500
        self.fall_speed = random.randint(60,90)
        if Flame.image == None:
           Flame.image = load_image('flame.png')

    def update(self, frame_time):
         self.y -= frame_time * self.fall_speed

    def stop(self):
        self.fall_speed = 0

    def get_bb(self):
         return self.x - 25, self.y - 25, self.x + 25, self.y + 25


    # fill here
