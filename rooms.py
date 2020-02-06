# Rooms
from sys import exit
from random import randint
from textwrap import dedent
prompt = "~> "
valid_move = "Please choose a valid option -> (h, j, k, l)\n~>"
# have classes pass through a parent to check if they can be entered

class Introduction(object):
    def enter(self):
        print(dedent("""
            This game will allow you to choose between good and bad
            Your choices will determine if you'll enter Heaven or Hell
            ---------------------------------------
            The directions to move are as follows:
            h will move left
            j will move back
            k will move forward
            l will move right
            ---------------------------------------
            There's a magical door right in front of you
            """))

        action = input(prompt)

        while True:

            if action == 'forward':
                print("The door you came out of slammed shut behind you and disappeared")
                return 'cabin_main_room'
        
            else:
                action = input(valid_move)


class CabinMainRoom(object):
    def enter(self):
        print(dedent("""
            You are standing in the entrance of a cabin
            To your right there is a bathroom
            """))
    
class Bathroom(object):
    
    def enter(self):
        print("working 2")
        return 'cabin_bedroom'

class CabinBedroom(object):

    def enter(self):
        print("working 3")
