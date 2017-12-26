import random

from pico2d import *

class Snow:

    image = None;

    SPEED = None
    snowSound = None
    def __init__(self):
        self.x, self.y = random.randint(20, 780), 590
        self.SPEED = random.randint(50,200)
        if Snow.image == None:
            Snow.image = load_image('bigsnow.png')
        if Snow.snowSound == None:
            Snow.snowSound = load_music('bbi.mp3')
            Snow.snowSound.set_volume(10)

    def update(self, frame_time):
        self.y -= (self.SPEED * frame_time)


    def draw(self, frame_time):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def resetSnow(self):
        self.snowSound.play()
        self.x, self.y = random.randint(20, 780), 590
        self.SPEED = random.randint(50, 200)
    def groundReset(self):
        self.x, self.y = random.randint(20, 780), 590
        self.SPEED = random.randint(50, 200)
