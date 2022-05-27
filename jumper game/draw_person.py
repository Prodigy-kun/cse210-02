# A class(draw_person) that draws the jumper dead and alive
class Draw_person:
    #attributes(none)
    # methods:person_alive()
    #          person_dead
    def person_alive(self):
        """Args:
            self (Die): An instance of Die.
        """
        #draw the person while alive
        print('   0   ')
        print('  /|\\')
        print('  / \\')

    def person_dead(self):
        """Args:
            self (Die): An instance of Die.
        """
         #draw the person while dead
        print('   x   ')
        print('  /|\\')
        print('  / \\')


