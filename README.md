# SekiroBot
Python controller for Sekiro: Shadows Die Twice. 
Includes a farming bot routine for a specific location.
This is a very simple program only capable of simple sequential commands.

# Installation
Install Python
Install pydirectinput library
Download and unzip this repository

# Setup
After killing the divine dragon, go to the "Ashina Outskirts - Outskirts Wall - Stairway" idol.
Verify the monitor running the game is set as your main monitor within your OS.
Change your in-game keyboard bindings to match the following:
    Note: If you do not want to change your keybinds, go through the sekiro.py file and change all references to the key(s).
    Movement:
        Slow Movement Shift = alt
        Move Forward = w
        Move Back = s
        Move Left = a
        Move Right = d
        Step Dodge, (hold) Sprint = shift
        Jump = space
        Crouch/Release Crouch = q
    Camera Controls:
        camera up = up arrow key
        camera down = down arrow key
        camera left = left arrow key
        camera right = right arrow key
        Camera Reset/Lock On = m
    Change Equipment:
        Cycle Quick Items (Forward) = x
        Cycle Quick Items (Reverse) = c
        Cycle Prosthetic Tool = z
    Attack Action:
        Attack = n
        Use Prosthetic Tool = ctrl
        Deflect, (Hold) Guard = Unbound (You don't need to unbind it, this is just my setting.)
        Grappling Hook = f
        Action, (hold) Collect Loot = e
        Use Item = r
        Eavesdrop/Touch Remnant = v
    Remnants:
        Remnant Menu/Stop Recording = g
Verify the following in-game settings:
    Note: Most of these will likely not affect the function of the script, but this is the only tested configuration.
    Game Options:
        Toggle auto lock-on: off
        Auto-target: off
        Controller vibration: 10
    Camera Options:
        Camera Y-axis: Standard
        Camera X-axis: Standard
        Reset camera Y-axis: Off
        Camera speed: 5
    Graphics Options:
        Screen Mode: Fullscreen
        Screen Resolution: 2560x1440
        Automatic Rendering Adjustment: Off

# Use
Equip the "Homeward Idol" on your item action bar and scroll to it so it is selected.
    Time how long it takes for your game to load after using the idol in this location.
    If it takes longer than 15 seconds, change the "wait_time" variable in sekiroFarm2.py's "use_idol()" function.
Pause the game and slide your mouse onto your second monitor, start the "sekiroFarm2.py" program.
You will see output in your terminal that the program has started and a 5 second countdown.
Slide your mouse back to Sekiro, click to regain focus on that window, exit the menu.