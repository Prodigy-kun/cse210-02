class Action:
    """An action that is done.
    
    The responsibility of action is to do somthing within in the game.
    It has one method, execute(), which should be overridden by derived classes.
    """
    def execute(self, cast, scripts):
        """Executes something that is important in the game. Method to be overidden.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        pass
