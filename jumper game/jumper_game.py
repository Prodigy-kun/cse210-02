from timeit import repeat


class Game:
    def __init__(self, word):
        """
        Initialize the game with the word to guess.

        :type  word: str
        :param word: the word to guess.
        """
        self._word = word
        self.board = []
        for i in range(len(word)):
            self.board.append("_ ")

        
    def check_guess(self, guess):
        """Check user input guess with answer
        assign correct letters to board property

        Args:
            guess (_str_): word given from user
        """

        for i in range(len(self._word)):
            if guess == self._word[i]:
                #print(f"{guess[i]} ", end = "")
                self.board.pop(i)
                self.board.insert(i, f"{guess} ")

    def print_board(self):
        # Display the starting board and correctly guessed letters after user guesses
        for x in range(len(self.board)):
            print (self.board[x], end=" ")
        print()

    def incorrect_guess(self, guess):
        if guess not in self._word:
            return True
         
    def correct_guess(self):
        board = ""
        for i in range(len(self.board)):
            board += self.board[i].strip(" ")
        if board == self._word:
            return True

                

