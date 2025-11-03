from pico2d import load_image, get_time, load_font
import random
import game_world
import game_framework
from state_machine import StateMachine


PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
FLY_SPEED_KMPH = 20.0 # Km / Hour
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Bird:
    image = None

    def __init__(self):
        self.x = random.randint(100, 500)
        self.y = random.randint(300, 500)
        self.dir = 1
        self.image = load_image('bird_animation.png')
        pass

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(0, 0, 92, 70, 0, ' ', self.x, self.y)
        elif self.dir == -1:
            self.image.clip_draw(92, 0, 92, 70, 0, 'v', self.x, self.y)



    def update(self):
        
        if self.x < 50:
            self.dir = 1
        elif self.x > 1550:
            self.dir = -1

