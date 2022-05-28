import random


def main():
    a = Alphabet()
    b = a.make_dash()
    c =

    print(b)
    print()
    print()

class Alphabet:
    def __init__(self):
        self.word_list= ['boy', 'horse', 'stop']
        self.chosen = random.choice(self.word_list)
        self.dash= []

    def make_dash(self):
        for i in range(len(self.chosen)):
            self.dash.append('_')
        return self.dash

    def print_dash(self):
        for dash in self.dash:
            print('-', end='')

class Terminal_service:
    def __init__(self):
        pass
    

    def ask_user(self, prompt):
        quest = input(prompt)
        return quest

main()