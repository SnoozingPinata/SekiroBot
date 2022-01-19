# SekiroBot
A simple Python farming bot for Sekiro: Shadows Die Twice for "Ashina Outskirts - Outskirts Wall - Stairway" location.
**You must progress the game to just before the final boss fight in order to use this farming bot.**

Click the image below to see the bot in action:

[![Alt text](https://img.youtube.com/vi/1Zt0m8rysnQ/0.jpg)](https://www.youtube.com/watch?v=1Zt0m8rysnQ)

# Installation
- Install Python 3+
- Install PyDirectInput library: `pip install PyDirectInput`
- Download and unzip this repository

# Setup
- Verify the monitor running the game is set as your main monitor within your OS.
- Change your in-game keyboard bindings to match for the following commands:
    - Note: If you do not want to change your keybinds, you can edit the key mapping in the sekiro.py file to match your keybinds.
    - Movement:
        - Slow Movement Shift = alt
        - Move Forward = w
        - Move Back = s
        - Move Left = a
        - Move Right = d
        - Jump = space
        - Crouch/Release Crouch = q
    - Camera Controls:
        - Camera Up = up arrow key
        - Camera Down = down arrow key
        - Camera Left = left arrow key
        - Camera Right = right arrow key
        - Camera Reset/Lock On = m
    - Attack Action:
        - Attack = n
        - Grappling Hook = f
        - Action, (hold) Collect Loot = e
        - Use Item = r
- Verify the following in-game settings:
    - Note: This script should work with other resolutions, but 2560x1440 is the only tested configuration.
    - Game Options:
        - Toggle auto lock-on: off
        - Auto-target: off
    - Camera Options:
        - Camera Y-axis: Standard
        - Camera X-axis: Standard
        - Reset camera Y-axis: Off
        - Camera speed: 5
    - Graphics Options:
        - Screen Mode: Fullscreen
        - Screen Resolution: 2560x1440
        - Automatic Rendering Adjustment: Off

# Use
- After killing the divine dragon, go to the "Ashina Outskirts - Outskirts Wall - Stairway" idol and rest at it.
- Equip the "Homeward Idol" on your item action bar and scroll to it so it is selected.
    - Time how long it takes for your game to load after using the idol in this location.
    - If it takes longer than 15 seconds, change the "wait_time" variable in sekiroFarm2.py's "use_idol()" function.
- Pause the game and run the "sekiroFarm2.py" program.
    - You will see output in your terminal that the program has started and a 10 second countdown has begun.
- Go back to Sekiro and unpause the game.
- Review how much experience and gold you are receiving from a single kill and edit the following variables within sekiroFarm2.py's "print_farm_report()" function:
    - "money_from_kill"
    - "exp_from_kill"