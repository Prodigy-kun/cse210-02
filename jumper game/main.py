from word_list import Word_list
from draw_person import Draw_person
from parachute import Parachute
from jumper_game import Game

def main():
    person = Draw_person()
    parachute = Parachute()
    words = Word_list()

    word = words.get_word()
    jumper = Game(word)
    while not parachute.game_over() and not jumper.correct_guess():

        jumper.print_board()
        parachute.draw_parachute()
        person.person_alive()
        guess = input("Enter your guess: ")
        jumper.check_guess(guess)
        if jumper.incorrect_guess(guess):
            parachute.delete_segment()
    if parachute.game_over():
        person.person_dead()
        print("You lost")
    else:
        jumper.print_board()
        print("You won")


if __name__=="__main__":
    main()


