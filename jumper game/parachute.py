class Parachute:
    '''
    Initial drawing: 
      ___
     /___\\
    \\   /
     \\ /

    '''
    def __init__(self) -> None:
        self._draw = ["  ___"," /___\\"," \\   /","  \\ /"]

    '''
     Draw parachute
    '''
    def draw_parachute(self):
        for i in self._draw:
            print(i)

    '''
     Delete one segment
    '''
    def delete_segment(self):
        self._draw.pop(0)

        '''True if there is no more parachute'''
    def game_over(self):
        return self._draw == []


