from constants import *
from casting.point import Point
from scripting.action import Action


class MovePaddleRAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        paddle_r = cast.get_first_actor(PADDLE_R_GROUP)
        body = paddle_r.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        
        position = position.add(velocity)

        if x < 0:
            position = Point(0, position.get_y())
        elif x > (SCREEN_WIDTH - PADDLE_WIDTH):
            position = Point(SCREEN_WIDTH - PADDLE_WIDTH, position.get_y())
            
        body.set_position(position)
        