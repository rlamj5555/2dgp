import random
import json
import os

from pico2d import *

from snow import Snow
from bucket import Bucket
from ground import Ground
from fire import Fire
from score import Score

import game_framework
import title_state
import gameclear
import gameover

name = "MainState"

backgroundImage = None

snows = None
bucket = None
ground = None
fires = None
score = None

count = 0

time = 0

def collide(a,b):
    left_a,bottom_a,right_a,top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def create_world():
    global snows, bucket, ground, fires, time, score
    time = 0
    bucket = Bucket()
    ground = Ground()
    snows = [Snow() for i in range(15)]
    fires = [Fire() for i in range(5)]
    score = Score()
    pass

def destroy_world():
    global snows, bucket, ground,fires, time

    del(snows)
    del(bucket)
    del(ground)
    del(fires)
    del(score)

def enter():
    print("Stage1")
    global backgroundImage
    backgroundImage = load_image('stage1_bg.png')
    create_world()

    pass


def exit():

    pass


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            bucket.handle_event(event)


def update(frame_time):
    global count, time
    bucket.update(frame_time)

    for snow in snows:
        snow.update(frame_time)
        if collide(ground,snow):
            snow.groundReset()
        if collide(bucket,snow):
            snow.resetSnow()
            bucket.getSnow()
            count += 1

    for fire in fires:
        fire.update(frame_time)
        if collide(ground,fire):
            fire.groundReset()
        if collide(bucket,fire):
            fire.resetFire()
            bucket.getFire()
    if 100 <= count:
        game_framework.change_state(gameclear)
        count = 0
        time = 0
    elif 60 < time:
        count = 0
        time = 0
        game_framework.change_state(gameover)



def draw(frame_time):
    global time, count
    time += frame_time
    clear_canvas()
    backgroundImage.draw(400,300)
    bucket.draw()

    Bucket.font.draw(375,460,'%3.2f'%time,(255,255,255))
    score.font.draw(25,275,'%1.0f'%count,(255,255,255))
    for snow in snows:
        snow.draw(frame_time)


    for fire in fires:
        fire.draw(frame_time)


    update_canvas()





