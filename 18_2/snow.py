import random

from pico2d import *

class Snow:

    image = None;

    def __init__(self):
        self.x, self.y = random.randint(150, 750), 500
        self.fall_speed = random.randint(150, 190)
        if Snow.image == None:
            Snow.image = load_image('small snow.png')

    def update(self, frame_time):
         self.y -= frame_time * self.fall_speed

    def draw(self):
        self.image.draw(self.x, self.y)


    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        #return self.x - 30, self.y - 30, self.x + 30, self.y + 30
        return self.x - 20, self.y - 40, self.x + 20, self.y - 20




class Bigsnow(Snow):
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
         return self.x - 20, self.y - 40, self.x + 20, self.y -20


class Flame(Snow):
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
        # return self.x - 25, self.y - 25, self.x + 25, self.y + 25
        return self.x - 20, self.y - 40, self.x + 20, self.y - 20



