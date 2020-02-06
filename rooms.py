# Rooms
from sys import exit
from random import randint
from textwrap import dedent
from player_stats import *
prompt = "~> "
valid_move = "Please choose a valid option -> (h, j, k, l)\n~>"
# have classes pass through a parent to check if they can be entered

# Tasks to be completed

completed = {
        'drugs': False
        }

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
            When presented with a choice to do something:
            yes will agree to something
            no will disagree to something
            ---------------------------------------
            There's a magical door right in front of you
            """))

        action = input(prompt)

        while True:

            if action == 'k':
                print("The door you came out of slammed shut behind you and disappeared")
                return 'cabin_main_room'
            else:
                action = input(valid_move)


class CabinMainRoom(object):
    def enter(self):
        print(dedent("""
            You are standing in the entrance of a cabin
            To your right there is a bathroom
            Behind you is a bedroom
            In front of you is a door to leave the cabin
            """))

        action = input(prompt)

        while True:
            if action == 'k':
                print("develop")
            elif action == 'l':
                return 'cabin_bathroom'
            elif action == 'j':
                return 'cabin_bedroom'
            else:
                action = input(valid_move)
class Bathroom(object):
    
    def enter(self):
        if completed['drugs'] == False:
            print(dedent("""
                There is a drug in the bathroom that is only precribed to people with cancer
                Do you take it?
                Taking it will decrease your morality by 5
                """))
            action = input(prompt)
            if action == 'yes':
                completed['drugs'] = True
                player.morality -= 5
                print(player.morality)

class CabinBedroom(object):

    def enter(self):
        print("working 3")
