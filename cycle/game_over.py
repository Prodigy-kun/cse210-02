from color import Color
 
class game_over():

    def __init__(self):
        self._color = Color(255,255,255)
        self._text = "Game over"

    def get_text(self):
        return self._text

    def get_color(self):
        return self._color