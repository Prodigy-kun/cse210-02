from point import Point
from actor import Actor

class Rock(Actor):
    
    def __init__(self):
        super().__init__()
        self.dy = 0
        self.dx = 0
        
    def get_x(self):

        return self.dx
            
    def get_y(self):
        
        return self.dy