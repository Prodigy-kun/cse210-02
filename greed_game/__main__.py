import os

from actor import Actor
from gem import Gem
from rock import Rock
from cast import Cast

from director import Director

from keyboardservice import KeyboardService
from videoservice import VideoService

from color import Color 
from point import Point

FRAME_RATE = 15
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed Game"
WHITE = Color(255, 255, 255)


def main():
    # Create cast of objects and players
    cast = Cast()

    # Create scoreboard

    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    position = Point(MAX_X/2, MAX_Y/2)

    player = Actor()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("players", player)

    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)
    
if __name__ == "__main__":
    main()