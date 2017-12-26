import game_framework
import title_state
from pico2d import *


name = "TitleState"
image = None



def enter():
    global image
    image = load_image('map_select.png')


def exit():
    global image
    del(image)


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
                title_state.stage = title_state.map1
                game_framework.change_state(title_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_2):
                title_state.stage = title_state.map2
                game_framework.change_state(title_state)


def draw(frame_time):
    clear_canvas()
    image.draw(400,300)
    update_canvas()







def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass






