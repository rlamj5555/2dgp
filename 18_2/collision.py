from pico2d import *

import game_framework


from bucket import Bucket
from snow import Smallsnow, Bigsnow, Flame
from background import Background




name = "collision"

bucket = None
smallsnows = None
bigsnows = None
background = None
flames=None

def create_world():
    global bucket, background, smallsnows, bigsnows, flames
    bucket = Bucket()
    bigsnows = [Bigsnow() for i in range(2)]
    smallsnows = [Smallsnow() for i in range(3)]
    flames = [Flame() for i in range(2)]
    smallsnows = bigsnows + smallsnows +flames
    background = Background()




def destroy_world():
    global bucket, background, smallsnows, bigsnows, flames

    del(bucket)
    del(smallsnows)
    del(background)
    del(bigsnows)
    del(flames)



def enter():
    open_canvas()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()



def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                bucket.handle_event(event)



def collide(a, b):

    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True



def update(frame_time):
    bucket.update(frame_time)
    for snow in smallsnows:
        snow.update(frame_time)

    for snow in smallsnows:
        if collide(bucket, snow):
            smallsnows.remove(snow)

    for snow in smallsnows:
         if collide(background, snow):
             smallsnows.remove(snow)

    for snow in flames:
         if collide(background, snow):
             flames.remove(snow)




def draw(frame_time):
    clear_canvas()
    background.draw()
    bucket.draw()
    for snow in smallsnows:
        snow.draw()

    background.draw_bb()
    bucket.draw_bb()
    for snow in smallsnows:
        snow.draw_bb()




    update_canvas()






