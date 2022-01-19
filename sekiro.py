import pydirectinput
import time

key_map = {
    "slow movement shift" : 'alt',
    "move forward" : 'w',
    "move back" : 's',
    "jump" : 'space',
    "crouch/release crouch" : 'q',
    "camera up" : 'up',
    "camera left" : 'left',
    "camera right" : 'right',
    "camera reset/lock on" : 'm',
    "attack" : 'n',
    "grappling hook" : 'f',
    "action, (hold) collect loot" : 'e',
    "use item" : 'r',
}


## Controller interface for the player character.
# walking controls
def walk_forward(seconds):
    pydirectinput.keyDown(key_map["move forward"])
    time.sleep(seconds)
    pydirectinput.keyUp(key_map["move forward"])

def walk_forward_hold_start():
    pydirectinput.keyDown(key_map["move forward"])

def walk_forward_hold_stop():
    pydirectinput.keyUp(key_map["move forward"])

def walk_backwards(seconds):
    pydirectinput.keyDown(key_map["move back"])
    time.sleep(seconds)
    pydirectinput.keyUp(key_map["move back"])

def walk_slow_start():
    pydirectinput.keyDown(key_map["slow movement shift"])

def walk_slow_stop():
    pydirectinput.keyUp(key_map["slow movement shift"])


# action controls
def toggle_stealth():
    pydirectinput.press(key_map["crouch/release crouch"])

def jump():
    pydirectinput.press(key_map['jump'])

def interact_hold(seconds):
    pydirectinput.keyDown(key_map["action, (hold) collect loot"])
    time.sleep(seconds)
    pydirectinput.keyUp(key_map["action, (hold) collect loot"])

def attack():
    pydirectinput.press(key_map["attack"])

def grapple(travel_time):
    pydirectinput.press(key_map["grappling hook"])
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
    pydirectinput.press(key_map["use item"])


# camera controls
def _camera_horizontal_seconds_for_degree(angle):
    # 90 degrees is almost exactly .4 seconds.
    # This is not perfectly accurate! 
    # It worked well enough for me that I didn't have to tune this.
    return (angle / 90) * .4

def camera_lock():
    pydirectinput.press(key_map["camera reset/lock on"])

def camera_left(degrees):
    seconds = _camera_horizontal_seconds_for_degree(degrees)
    pydirectinput.keyDown(key_map["camera left"])
    time.sleep(seconds)
    pydirectinput.keyUp(key_map["camera left"])

def camera_right(degrees):
    seconds = _camera_horizontal_seconds_for_degree(degrees)
    pydirectinput.keyDown(key_map["camera right"])
    time.sleep(seconds)
    pydirectinput.keyUp(key_map["camera right"])

def camera_up(degrees):
    # I only needed this function for one small part so I didn't make a vertical translator function.
    seconds = _camera_horizontal_seconds_for_degree(degrees)
    pydirectinput.keyDown(key_map["camera up"])
    time.sleep(seconds)
    pydirectinput.keyUp(key_map["camera up"])


# menu controls
def menu_down():
    pydirectinput.press('down')
    
def menu_select():
    pydirectinput.press('enter')