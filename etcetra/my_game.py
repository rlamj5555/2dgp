from pico2d import *
import random
import game_framework

running = None
bucket = None




class Smallsnow:
    def __init__(self):
        self.x, self.y = random.randint(200, 750), 600
        self.image = load_image('small snow.png')
        self.Speed = random.randint(3,10)

    def update(self):
        if self.y >= -50:
            self.y -= self.Speed

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x-10, self.y-10, self.x+10, self.y+10

class Bigsnow:
    def __init__(self):
        self.x, self.y = random.randint(200, 750), 600
        self.image = load_image('big snow.png')
        self.Speed = random.randint(3,10)

    def update(self):
        if self.y >= -50:
            self.y -= self.Speed

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10


class Flame:
    def __init__(self):
        self.x, self.y = random.randint(200, 750), 600
        self.image = load_image('flame.png')
        self.Speed = random.randint(3,10)

    def update(self):
        if self.y >= -70:
            self.y -= self.Speed

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

class Background:
    def __init__(self):
        self.image = load_image('white_bg.png')

    def draw(self):
        self.image.draw(400, 300)


class Bucket:
    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3


    def __init__(self):
        self.x, self.y = random.randint(100, 700), 130
        self.frame = random.randint(0, 7)
        self.state = self.RIGHT_STAND
        if Bucket.image == None:
            Bucket.image = load_image('bucket_sheet.png')

    def handle_event(self, event):
        if(event.type, event.key)==(SDL_KEYDOWN, SDLK_LEFT):
            if self.state in(self.RIGHT_STAND, self.LEFT_STAND):
                self.state = self.LEFT_RUN
        elif(event.type, event.key)==(SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in(self.RIGHT_STAND, self.LEFT_STAND):
                self.state=self.RIGHT_RUN
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state = self.LEFT_STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state = self.RIGHT_STAND

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10


    def update(self):
        self.frame=(self.frame+1)%8
        if self.state==self.RIGHT_RUN:
            self.x=min(750,self.x+30)
        elif self.state==self.LEFT_RUN:
            self.x=max(150,self.x-30)


    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)


def handle_events():
    global running
    global bucket
    global x
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            bucket.handle_event(event)



def main():

    open_canvas()
    smallsnow = [Smallsnow() for i in range(6)]
    bigsnow = [Bigsnow() for i in range(3)]
    flame = [Flame() for i in range(4)]

    global bucket
    global running

    bucket = Bucket()
    background = Background()

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

        for iter in bigsnow:
            iter.update()

        for liter in bigsnow:
            iter2.update()

        bucket.update()

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

        bucket.draw()
        update_canvas()

        delay(0.05)

    close_canvas()


if __name__ == '__main__':
    main()