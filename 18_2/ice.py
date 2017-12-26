import random

from pico2d import *

class Ice:

    image = None;

    SPEED = None
    IceSound = None
    def __init__(self):
        self.x, self.y = random.randint(20, 780), 590
        self.SPEED = random.randint(50,200)
        if Ice.image == None:
            Ice.image = load_image('icecube.png')
        if Ice.IceSound == None:
            Ice.IceSound = load_music('bbi.mp3')
            Ice.IceSound.set_volume(32)

    def update(self, frame_time):
        self.y -= (self.SPEED * frame_time)


    def draw(self, frame_time):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def resetIce(self):
        self.IceSound.play()
        self.x, self.y = random.randint(20, 780), 590
        self.SPEED = random.randint(50, 200)
    def groundReset(self):
        self.x, self.y = random.randint(20, 780), 590
        self.SPEED = random.randint(50, 200)
