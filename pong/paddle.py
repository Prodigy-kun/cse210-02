import constants as constants
from actor import Actor
from point import Point
import random

from pong.constants import CELL_SIZE

class Paddle(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self._segments = []
        self._prepare_body()

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)
    
    def _prepare_body(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / (constants.MAX_Y/CELL_SIZE))

        for i in range(constants.PADDLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "#"
            color = constants.YELLOW
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)