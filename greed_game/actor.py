from color import Color
from point import Point

class Actor:

    def __init__(self):
        """Constructs a new Actor."""
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def get_color(self):
        return self._color

    def get_font_size(self):
        return self._font_size

    def get_position(self):
        return self._position

    def get_velocity(self):
        return self._velocity
    
    def move_y(self, speed):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given y value.
        """
        x = self._position.get_x()
        y = self._position.get_y() + speed
        self._position = Point(x, y)
    
    def move_x(self, max_x):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = 550
        self._position = Point(x, y)
        
    def set_color(self, color):
        self._color = color

    def set_position(self, position):
        self._position = position
    
    def set_font_size(self, font_size):
        self._font_size = font_size

    def set_velocity(self, velocity):
        self._velocity = velocity
        
    def set_text(self, text):
        """Updates the text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._text = text
        
    def get_text(self):
        
        return self._text
    
    def get_y(self):
        
        return self._position.get_y()