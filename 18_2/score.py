from pico2d import *

class Score:
    font = None
    def __init__(self):
        if Score.font == None:
            Score.font = load_font('OpenSansLight.TTF', 32)
        pass

    def draw(self):
        pass

