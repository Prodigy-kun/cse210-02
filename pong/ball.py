import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Ball(Actor):
    def __init__(self):
        "Constructs a new Food."
        super().__init__()
        self.set_text("@")
        self.set_color(constants.RED)
        self.reset()
        
    def reset(self):
        """Selects a random position where the ball re-appears"""
        # x = random.randint(1, constants.COLUMNS - 1)
        # y = random.randint(1, constants.ROWS - 1)
        x = (constants.COLUMNS)/2
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
        