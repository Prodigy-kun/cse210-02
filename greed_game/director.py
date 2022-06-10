from color import Color
from point import Point
from gemt import Gem
from rock import Rock

import random
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
MAX_OBJECTS = 80
MAX_Y = 610

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._points = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_outputs(cast)
            self._draw_points(cast)
            self._draw_objects(cast)
            self._do_updates(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _draw_points(self, cast):
        banner = cast.get_first_actor("banners")
        banner.set_text(f"Score{self._points}")

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        gems = cast.get_actors("gems")
        rocks = cast.get_actors("rocks")
        max_x = self._video_service.get_width()
        robot.move_x(max_x)
        y_speed = 5
        for gem in gems:
            gem.move_y(y_speed)
            if robot.get_position().equals(gem.get_position()):
                self._points += 1
                cast.remove_actor("gems", gem)
            if gem.get_y() > MAX_Y:
                cast.remove_actor("gems", gem)
                
        for rock in rocks:
            rock.move_y(y_speed)
            if robot.get_position().equals(rock.get_position()):
                self._points -= 1
                cast.remove_actor("rocks", rock)
            if rock.get_y() > MAX_Y:
                cast.remove_actor("rocks", rock)
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
        
    def _draw_objects(self, cast):
        if len(cast.get_all_actors()) < MAX_OBJECTS:
            x = random.randint(1, COLS - 1)
            y = random.randint(1, ROWS / 2)
            position = Point(x, y)
            position = position.scale(CELL_SIZE)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)
            
            gem = Gem()
            gem.set_text("*")
            gem.set_font_size(FONT_SIZE)
            gem.set_color(color)
            gem.set_position(position)
            cast.add_actor("gems", gem)
        
            x = random.randint(1, COLS - 1)
            y = random.randint(1, ROWS / 2) 
            position = Point(x, y)
            position = position.scale(CELL_SIZE)
            
            r = 165
            g = 42
            b = 42
            color = Color(r, g, b)
            rock = Rock()
            rock.set_text("O")
            rock.set_font_size(FONT_SIZE)
            rock.set_color(color)
            rock.set_position(position)
            cast.add_actor("rocks", rock)