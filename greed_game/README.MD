# GREED GAME
Greed is a game in which the player seeks to gather as many falling gems as possible. The game continues as long as the player wants more!

# RULES
'''Gems (*) and rocks (o) randomly appear and fall from the top of the screen.
The player (#) can move left or right along the bottom of the screen.
If the player touches a gem they earn a point.
If the player touches a rock they lose a point.
Gems and rocks are removed when the player touches them.
The game continues until the player closes the window.'''

'''Requirements'''
'''The program must include a README file.
The program must include class and method comments.
The program must remain true to game play described in the overview.'''

'''Required Technologies'''
'''Python 3.8.0'''

# Authors
'''
Tim Smith
Kevin del Hoyo
Omotayo Promise
Robert Elliott
'''

# classes and outline

class Actor()
    Parent class of Gems and rocks
    Kevin
    __init__
        self._text
        self._font_size
        self._color
        self._position
        self._velocity

    get_color
        return self._color
    
    font_size
        return self._font_size

    get_position
        return position

    movement
        move actor to next position
        Actors only move downward

    set_color
        sets color of actor

    set_position
        sets position of actor

    set_font
        sets font size of actor

    set_text
        updates text of actor

    set_velocity
        updates velocity of actor

    remove_actor
        removes actor when it touches a player

class Rocks(Actor)
    Timothy
    inherit init from actor

class Gems(actor)
    Robert
    inherit from actor

class player    
    Timothy
    init
        x position
        color
        symbol

    move_player
        moves the player left or right by changing x position

class Director
    Robert
    init   
        self.points

    is_touching
        checks if a player is touching a gem or rock

    gain_point
        gain 1 if touching a gem

    lose_point
        lose 1 if touching a rock

    start_game
        starts the start_game

    update
        updates the players _position

class VideoService
    Promise
    init
        caption
        game borders
        frame rate
        debug
        cell size

    close_window
        closes game

    See VideoService from RFK as template

class KeyboardService
    Promise
    See KeyboardService from RFK as template

class Cast
    Kevin
    keep track of all actors and artifacts
    see Cast class from RFK as template