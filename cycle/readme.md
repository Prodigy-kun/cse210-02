# Cycle
Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them.

# Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 cycle
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

# Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- cycle              (source code for game)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7
# Authors
Tim Smith
Kevin del Hoyo
Omotayo Promise
Robert Elliott
'''

# Tim:
    class ControlActorsAction(Action)

    Copy from game
    change the controls (i, j, k, l / a, s, d, w)


    class DrawActorsAction(Action)

    class HandleCollisionsAction(Action)

    class MoveActorsAction(Action)

# Promise:
    
    class snake(Actor)
        COPY

    class Script

    class KeyboardService

    class VideoService

# Robert:
    class Color

    class Point

    
    class Cast
        see snake game

    
    class Action

# Kevin:
    class Game_over
        display a message
        return true when the game is over

    class actor()
        copy from snake game

    class score(Actor)
         COPY 

    class director

