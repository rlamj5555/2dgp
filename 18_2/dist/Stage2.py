import random
import json
import os

from pico2d import *

from ice import Ice
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

ices = None
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
    global ices, bucket, ground, fires, time, score
    time = 0
    bucket = Bucket()
    ground = Ground()
    ices = [Ice() for i in range(15)]
    fires = [Fire() for i in range(5)]
    score = Score()
    pass

def destroy_world():
    global ices, bucket, ground,fires, time

    del(ices)
    del(bucket)
    del(ground)
    del(fires)
    del(score)

def enter():
    print("Stage1")
    global backgroundImage
    backgroundImage = load_image('stage2_bg.png')
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

    for ice in ices:
        ice.update(frame_time)
        if collide(ground,ice):
            ice.groundReset()
        if collide(bucket,ice):
            ice.resetIce()
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
    score.font.draw(20,395,'%1.0f'%count,(255,255,255))
    for ice in ices:
        ice.draw(frame_time)


    for fire in fires:
        fire.draw(frame_time)


    update_canvas()





