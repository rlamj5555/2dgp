import random

from pico2d import *

class Fire:

    image = None;

    SPEED = None
    fireSound = None
    def __init__(self):
        self.x, self.y = random.randint(20, 780), 590
        self.SPEED = random.randint(50,200)
        if Fire.image == None:
            Fire.image = load_image('flame.png')
        if Fire.fireSound == None:
            Fire.fireSound = load_music('firesound.mp3')
            Fire.fireSound.set_volume(32)

    def update(self, frame_time):
        self.y -= (self.SPEED * frame_time)


    def draw(self, frame_time):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def resetFire(self):
        self.fireSound.play()
        self.x, self.y = random.randint(20, 780), 590
        self.SPEED = random.randint(50, 200)
    def groundReset(self):
        self.x, self.y = random.randint(20, 780), 590
        self.SPEED = random.randint(50, 200)
    # fill here
