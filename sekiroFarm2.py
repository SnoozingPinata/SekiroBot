import pydirectinput
import time
import sekiro


def countdown(seconds):
    print(f"\n\nStarting Sekiro Farmer bot in {seconds} seconds. Set window focus to the game and exit any menus.")
    for i in range(0, seconds):
        print(f" -- {i + 1}")
        time.sleep(1)
    print("Proceeding with farmbot...")

def use_idol():
    ### If your computer loads faster or slower, you may need to change this setting.
    # Just time how long it takes for your computer to load in and be ready and put that in here.
    wait_time = 18
    print(" -- Using Idol.")
    sekiro.item_use()
    pydirectinput.press('down')
    pydirectinput.press('enter')
    print(f" -- Waiting {wait_time} seconds for Loading Screen.")
    time.sleep(wait_time)

def bulwark_line_up():
    print(" -- Lining up with bulwark.")
    # turn left ~150 degrees
    sekiro.camera_left(130)
    sekiro.walk_slow_start()
    sekiro.walk_forward(4)
    sekiro.walk_slow_stop()

def bulwark_jump():
    print(" -- Jumping over bulwark.")
    sekiro.walk_slow_start()
    sekiro.walk_forward_hold()
    sekiro.jump()
    time.sleep(1)
    sekiro.walk_slow_stop()
    time.sleep(.8)
    sekiro.walk_forward_hold_stop()

def ledge_jump():
    print(" -- Jumping from ledge.")
    sekiro.walk_forward_hold()
    time.sleep(.8)
    sekiro.jump()
    sekiro.walk_forward_hold_stop()
    sekiro.grapple_repeat_for(.5, 2)

def platform_grapple():
    print(" -- Grappling to platform.")
    sekiro.camera_right(135)
    sekiro.walk_forward(1)
    sekiro.camera_up(45)
    sekiro.grapple(2)

def first_enemy_approach():
    print(" -- Approaching first enemy.")
    sekiro.walk_slow_start()
    sekiro.walk_forward(.2)
    sekiro.walk_slow_stop()

def kill_and_collect():
    print(" -- Killing and collecting loot.")
    sekiro.camera_lock()
    # main attack button to 1-hit kill, wait for death animation
    sekiro.attack()
    time.sleep(1.6)
    # collect item
    sekiro.interact_hold(1.2)

def platform_drop_off():
    print(" -- Dropping off platform.")
    sekiro.walk_backwards(1)
    sekiro.toggle_stealth()
    time.sleep(.2)

def second_platform_drop_off():
    print(" -- Dropping off second platform.")
    sekiro.walk_forward(1.2)
    time.sleep(.3)

def second_enemy_approach():
    print(" -- Approaching second enemy.")
    sekiro.camera_lock()
    sekiro.walk_slow_start()
    sekiro.walk_forward(.8)
    sekiro.walk_slow_stop()

def farm_route_instructions():
    use_idol()
    bulwark_line_up()
    bulwark_jump()
    ledge_jump()
    platform_grapple()
    first_enemy_approach()
    kill_and_collect()
    platform_drop_off()
    second_platform_drop_off()
    second_enemy_approach()
    kill_and_collect()

def print_farm_report(run_count):
    money_from_kill = 220
    exp_from_kill = 1854
    print("---------- Farm Bot Report ----------")
    print(f"  {run_count} succesful run(s) completed.")
    print(f"  {run_count * 2} kills.")
    print(f"  {run_count * (money_from_kill * 2)} money earned.")
    print(f"  {run_count * (exp_from_kill * 2)} experience points earned.\n")

if __name__ == "__main__":
    countdown(5)
    counter = 0
    while True:
        counter += 1
        print(f"\nBeginning run {counter}.")
        farm_route_instructions()
        print_farm_report(counter)
