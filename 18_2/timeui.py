# adjust_run_and_action.py : regulate run speed and action speed as well

import random
import json
from pico2d import *

running = None

class Timeui:


    font = None


    def __init__(self):
        self.x, self.y = 0, 90
        if Timeui.font == None:
            Timeui.font = load_font('OpenSans-Light.ttf', 30)


    def update(self, frame_time):
        pass

    def draw(self):
        Timeui.font.draw(self.x - 40, self.y + 170, 'Time %3.1f' %get_time(), (100, 700, 0))#170: 높이 조절



def handle_events(current_time):
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


current_time = 0.0


def get_frame_time():

    global current_time

    current_time = 0
    return current_time


def main():

    open_canvas(960, 272)

    global running
    global current_time


    timeui=Timeui()

    running = True
    current_time = get_time()

    while running:

        frame_time = get_frame_time()
        handle_events(frame_time)

        timeui.update(frame_time)

        # Game Rendering
        clear_canvas()

        timeui.draw()
        update_canvas()

