import pyray

class VideoService:


    def __init__(self, caption, width, height, cell_size, frame_rate, debug = False):
            """Constructs a new VideoService using the specified debug mode.
            
            Args:
                debug (bool): whether or not to draw in debug mode.
            """
            self._caption = caption
            self._width = width
            self._height = height
            self._cell_size = cell_size
            self._frame_rate = frame_rate
            self._debug = debug


    def open_window(self):
        """Opens a new window with the provided title.

        Args:
            title (string): The title of the window.
        """
        pyray.init_window(self._width, self._height, self._caption)
        pyray.set_target_fps(self._frame_rate)


    def close_window(self):
        """Closes the window and releases all computing resources."""
        pyray.close_window()


    def clear_buffer(self):
        """Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase.
        """
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()

    def _draw_grid(self):
        """Draws a grid on the screen."""
        for y in range(0, self._height, self._cell_size):
            pyray.draw_line(0, y, self._width, y, pyray.BLUE)
        for x in range(0, self._width, self._cell_size):
            pyray.draw_line(x, 0, x, self._height, pyray.BLUE)
            

    def flush_buffer(self):
        """Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.
        """ 
        pyray.end_drawing()
    
