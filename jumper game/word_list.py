import random

class Word_list:
    def __init__(self):
        self.word_list = ["blank", "chess", "games", "shoot", "stomp", "books", "erase", "raise", "great", "keeps"]
        
    def get_word(self):
        self.word = self.word_list[random.randint(0,9)]
        return self.word
    
list = Word_list()
word = list.get_word()
print(word)