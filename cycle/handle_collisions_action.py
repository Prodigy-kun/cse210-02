import constants
from actor import Actor
from action import Action
from point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_snake_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_snake_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        '''score = cast.get_first_actor("scores")
        snake2 = cast.get_first_actor("snakes2")
        snake = cast.get_first_actor("snakes")
        head = snake.get_head()
        head2 = snake2.get_head()
        

        if (head.get_position().equals(snake2.get_position()))or(snake.get_position().equals(head2.get_position())):
            #points = food.get_points()
            #snake.grow_tail(points)
            #score.add_points(points)
            #food.reset()
            self._handle_game_over(cast)'''
        
        snake2 = cast.get_first_actor("snakes2")
        snake = cast.get_first_actor("snakes")
        head = snake.get_segments()[0]
        head2 = snake2.get_segments()[0]
        segments = snake.get_segments()[1:]
        segments2 = snake2.get_segments()[1:]
        
        for i in range(len(segments)):
            if (head.get_position().equals(segments2[i].get_position()))or((head2.get_position().equals(segments[i].get_position()))):
                self._is_game_over = True
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake = cast.get_first_actor("snakes")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]
        
        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake = cast.get_first_actor("snakes")
            segments = snake.get_segments()
            #food = cast.get_first_actor("foods")
            snake2 = cast.get_first_actor("snakes2")
            segments2 = snake2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for i in range(len(segments)):
                segments[i].set_color(constants.WHITE)
                segments2[i].set_color(constants.WHITE)