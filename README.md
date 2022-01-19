# SekiroBot
Python farming bot for Sekiro: Shadows Die Twice for "Ashina Outskirts - Outskirts Wall - Stairway" location.
You must progress the game to just before the final boss fight in order to use this farming bot.

Link to bot farm showcase: https://youtu.be/1Zt0m8rysnQ

[![Alt text](https://img.youtube.com/vi/1Zt0m8rysnQ/0.jpg)](https://www.youtube.com/watch?v=1Zt0m8rysnQ)

# Installation
- Install Python
- Install pydirectinput library
- Download and unzip this repository

# Setup
- Verify the monitor running the game is set as your main monitor within your OS.
- Verify you are running the game in Full Screen.
- Change your in-game keyboard bindings to match for the following commands:
    - Note: If you do not want to change your keybinds, go through the sekiro.py file and change the key_map to match your binds.
    - Movement:
        - Slow Movement Shift = alt
        - Move Forward = w
        - Move Back = s
        - Move Left = a
        - Move Right = d
        - Jump = space
        - Crouch/Release Crouch = q
    - Camera Controls:
        - camera up = up arrow key
        - camera down = down arrow key
        - camera left = left arrow key
        - camera right = right arrow key
        - Camera Reset/Lock On = m
    - Attack Action:
        - Attack = n
        - Grappling Hook = f
        - Action, (hold) Collect Loot = e
        - Use Item = r
- Verify the following in-game settings:
    - Note: Most of these will likely not affect the function of the script, but this is the only tested configuration.
    - Game Options:
        - Toggle auto lock-on: off
        - Auto-target: off
        - Controller vibration: 10
    - Camera Options:
        - Camera Y-axis: Standard
        - Camera X-axis: Standard
        - Reset camera Y-axis: Off
        - Camera speed: 5
    - Graphics Options:
        - Screen Mode: Fullscreen
        - Screen Resolution: 2560x1440 (This shoud not matter.)
        - Automatic Rendering Adjustment: Off

# Use
- After killing the divine dragon, go to the "Ashina Outskirts - Outskirts Wall - Stairway" idol.
- Equip the "Homeward Idol" on your item action bar and scroll to it so it is selected.
    - Time how long it takes for your game to load after using the idol in this location.
    - If it takes longer than 15 seconds, change the "wait_time" variable in sekiroFarm2.py's "use_idol()" function.
- Pause the game and slide your mouse onto your second monitor, start the "sekiroFarm2.py" program.
- You will see output in your terminal that the program has started and a 5 second countdown.
- Slide your mouse back to Sekiro, click to regain focus on that window, exit the menu.
- Review how much experience and gold you are receiving from a single kill and edit the following variables within sekiroFarm2.py:
    - "money_from_kill"
    - "exp_from_kill"