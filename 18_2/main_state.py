from pico2d import *


import game_framework


from bucket import Bucket
from snow import Snow, Bigsnow, Flame
from background import Background
from timeui import Timeui





name = "main_state"

bucket = None
snows = None
bigsnows = None
background = None
flames=None
timeui = None



def create_world():
    global bucket, background, snows, bigsnows, flames, timeui
    bucket = Bucket()
    bigsnows = [Bigsnow() for i in range(2)]
    snows = [Snow() for i in range(3)]
    flames = [Flame() for i in range(2)]
    snows = bigsnows + snows + flames
    background = Background()
    timeui=Timeui()





def destroy_world():
    global bucket, background, snows, bigsnows, flames,timeui

    del(bucket)
    del(snows)
    del(background)
    del(bigsnows)
    del(flames)
    del(timeui)




def enter():
    open_canvas()
    global running
    global current_time
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
    for snow in snows:
        snow.update(frame_time)

    for snow in snows:
        if collide(bucket, snow):
            snows.remove(snow)
            bucket.meet(snow)



    for snow in bigsnows:
         if collide(background, snow):
             bigsnows.remove(snow)


    for snow in flames:
         if collide(background, snow):
             flames.remove(snow)




def draw(frame_time):
    clear_canvas()
    background.draw()
    bucket.draw()
    for snow in snows:
        snow.draw()

    background.draw_bb()
    bucket.draw_bb()
    for snow in snows:
        snow.draw_bb()




    update_canvas()






