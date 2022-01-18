import pydirectinput
import time

## Controller interface for the player character.
# walking controls
def walk_left(seconds):
    pydirectinput.keyDown('a')
    time.sleep(seconds)
    pydirectinput.keyUp('a')

def walk_right(seconds):
    pydirectinput.keyDown('d')
    time.sleep(seconds)
    pydirectinput.keyUp('d')

def walk_forward(seconds):
    pydirectinput.keyDown('w')
    time.sleep(seconds)
    pydirectinput.keyUp('w')

def walk_forward_hold():
    pydirectinput.keyDown('w')

def walk_forward_hold_stop():
    pydirectinput.keyUp('w')

def walk_backwards(seconds):
    pydirectinput.keyDown('s')
    time.sleep(seconds)
    pydirectinput.keyUp('s')

def walk_slow_start():
    pydirectinput.keyDown('alt')

def walk_slow_stop():
    pydirectinput.keyUp('alt')


# action controls
def toggle_stealth():
    pydirectinput.press('q')

def jump():
    pydirectinput.press('space')

def dodge():
    pydirectinput.press('shift')

def interact():
    pydirectinput.press('e')

def interact_hold(seconds):
    pydirectinput.keyDown('e')
    time.sleep(seconds)
    pydirectinput.keyUp('e')

def attack():
    pydirectinput.press('n')

def block():
    raise NotImplementedError

def grapple(travel_time):
    pydirectinput.press('f')
    time.sleep(travel_time)

def grapple_repeat_for(seconds, travel_time):
    grapple_attempt_wait_period = .25 ## .25 seconds
    amount_of_attempts = seconds * 4 # because wait period is 1/4th second
    for i in range(0, int(amount_of_attempts)):
        grapple(0)
        time.sleep(grapple_attempt_wait_period)
    time.sleep(travel_time)


# item controls
def item_use():
    pydirectinput.press('r')

def item_switch_right():
    raise NotImplementedError

def item_switch_left():
    raise NotImplementedError


# prosthesis controls
def prosthesis_switch():
    pydirectinput.press('z')

def prosthesis_use():
    pydirectinput.press('ctrl')


# camera controls
def _camera_horizontal_seconds_for_degree(angle):
    # 90 degrees is almost exactly .4 seconds, will need to fine tune.
    return (angle / 90) * .4

def camera_lock():
    pydirectinput.press('m')

def camera_left(degrees):
    seconds = _camera_horizontal_seconds_for_degree(degrees)
    pydirectinput.keyDown('left')
    time.sleep(seconds)
    pydirectinput.keyUp('left')

def camera_right(degrees):
    seconds = _camera_horizontal_seconds_for_degree(degrees)
    pydirectinput.keyDown('right')
    time.sleep(seconds)
    pydirectinput.keyUp('right')

def camera_up(degrees):
    seconds = _camera_horizontal_seconds_for_degree(degrees)
    pydirectinput.keyDown('up')
    time.sleep(seconds)
    pydirectinput.keyUp('up')

def camera_down(degrees):
    raise NotImplementedError