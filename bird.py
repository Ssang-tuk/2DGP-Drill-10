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
FRAMES_PER_ACTION = 14

class Bird:
    image = None

    def __init__(self):
        self.x = random.randint(100, 500)
        self.y = random.randint(300, 500)
        self.dir = 1
        self.change_y = 0
        self.change_x = 0
        self.frame = 0
        self.image = load_image('bird_animation.png')


    def draw(self):
        frame_index = int(self.frame)

        if frame_index < 5:
            self.change_y = 0
            self.change_x = frame_index
        elif frame_index < 10:
            self.change_y = 1
            self.change_x = frame_index - 5
        else:
            self.change_y = 2
            self.change_x = frame_index - 10

        if self.dir == 1:
            self.image.clip_composite_draw(self.change_x * 183, self.change_y * 168, 183, 168, 0, ' ', self.x, self.y, 80, 80)
        elif self.dir == -1:
            self.image.clip_composite_draw(self.change_x * 183, self.change_y * 168, 183, 168, 0, 'h', self.x, self.y, 80, 80)



    def update(self):

        self.frame += 12 * game_framework.frame_time

        if self.frame >= FRAMES_PER_ACTION:
            self.frame -= FRAMES_PER_ACTION

        self.x += self.dir * FLY_SPEED_PPS * game_framework.frame_time

        if self.x < 50:
            self.dir = 1
        elif self.x > 1550:
            self.dir = -1

