class Rocks(Actor):
    
    def __init__(self):
        super().__init__()
        self._message = ""
        
    def get_message(self):
        """Receives the rocks message(s).
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message