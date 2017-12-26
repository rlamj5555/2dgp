import game_framework
import Stage1
import Stage2
import  map_select_state
from pico2d import *


name = "TitleState"
image = None

stage = 0

map1 = 1
map2 = 2

def enter():
    global image
    image = load_image('title_state.png')


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
                game_framework.change_state(map_select_state)
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if(stage == map1):
                    game_framework.change_state(Stage1)
                elif(stage == map2):
                    game_framework.change_state(Stage2)

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






