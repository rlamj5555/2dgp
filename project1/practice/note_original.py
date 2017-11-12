from pico2d import *
import random


class bucket:
    def __init__(self):
        self.image=load_image('bucket.png')
    def draw(self):
        self.image.draw(500,500)



class background:
    def __init__(self):
        self.image = load_image('white_bg.png')
    def draw(self):
        self.image.draw(400, 300)


class smallsnow:
    def __init__(self):
        self.x, self.y = random.randint(200, 750), 600
        self.image = load_image('small snow.png')
        self.Speed = random.randint(3,10)

    def update(self):
        if self.y >= -50:
            self.y -= self.Speed

    def draw(self):
        self.image.draw(self.x, self.y)

class bigsnow:
    def __init__(self):
        self.x, self.y = random.randint(200, 750), 600
        self.image = load_image('big snow.png')
        self.Speed = random.randint(3,10)

    def update(self):
        if self.y >= -50:
            self.y -= self.Speed

    def draw(self):
        self.image.draw(self.x, self.y)



class flame:
    def __init__(self):
        self.x, self.y = random.randint(200, 750), 600
        self.image = load_image('flame.png')
        self.Speed = random.randint(3,10)

    def update(self):
        if self.y >= -70:
            self.y -= self.Speed

    def draw(self):
        self.image.draw(self.x, self.y)



class snowman:
    def __init__(self):
        self.x, self.y = random.randint(200, 750), 90
        self.image = load_image('small snowman.png')

    def update(self):
        self.x += 5


    def draw(self):
        self.image.draw(self.x, self.y)


open_canvas()

smallsnow = [smallsnow() for i in range(6)]
bigsnow = [bigsnow() for i in range(3)]
flame = [flame() for i in range(4)]
bucket=bucket()



background = background()
running = True
x=0

while running:
    handle_events()
    for iter in smallsnow:
        iter.update()

    for iter2 in smallsnow:
        iter2.update()

    for iter in flame:
        iter.update()

    for iter2 in flame:
        iter2.update()

    for iter  in bigsnow:
        iter.update()

    for liter in bigsnow:
        iter2.update()



    clear_canvas()
    background.draw()
    for iter in smallsnow:
        iter.draw()

    for iter2 in smallsnow:
        iter2.draw()

    for iter in flame:
        iter.draw()

    for iter2 in flame:
        iter2.draw()

    for iter in bigsnow:
        iter.draw()

    for iter2 in bigsnow:
        iter2.draw()




    update_canvas()
    delay(0.05)



close_canvas()