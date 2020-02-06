# Rooms
from sys import exit
from random import randint
from textwrap import dedent
from player_stats import *
prompt = "~> "
valid_move = "Please choose a valid option -> (h, j, k, l)\n~> "
valid_choice = "Please choose a valid option -> (yes, no)\n~> "
# have classes pass through a parent to check if they can be entered

# Tasks to be completed

completed = {
        'drugs': False,
        'cleaned_room': False,
        'kid_drowning': False
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
                return 'outside_cabin'
            elif action == 'l':
                return 'cabin_bathroom'
            elif action == 'j':
                return 'cabin_bedroom'
            elif action == 'h':
                print("You can't go that way")
                action = input(prompt)
            else:
                action = input(valid_move)

# Cabin Bathroom
class CabinBathroom(object):
    
    def enter(self):
        if completed['drugs'] == False:
            print(dedent("""
                There is a pill in the bathroom that is only precribed to people with cancer
                You don't have cancer
                Taking it will get you really high
                Do you take it?
                Taking it will decrease your morality by 5
                """))
            action = input(prompt)

            while True:
                if action == 'yes':
                    completed['drugs'] = True
                    player.morality -= 5
                    print(dedent("""
                        After taking the pill your whole body feels amazing
                        There is nothing else in the bathroom to use
                        Your morality is {player.morality}
                        """))
                    break

                elif action == 'no':
                    print(dedent(f"""
                        You refrained from stealing drugs
                        Your morality is {player.morality}
                        """))
                    break
                else:
                    action = input(valid_choice)
        
        print(dedent("""
            There is nothing else in the bathroom to use
            All you can do is head back
            """))

        action = input(prompt)

        while True:
            if action == 'j':
                return 'cabin_main_room'

            elif action == 'h' or action == 'k' or action == 'l':
                print("You can't go that way")
                action = input(prompt)

            else:
                action = input(valid_move)

class CabinBedroom(object):

    def enter(self):
        if completed['cleaned_room'] == False:
            print(dedent("""
                The bedroom is messy
                Do you clean it?
                Cleaning the bedroom will increase your morality by 3
                """))
            action = input(prompt)

            while True:
                if action == 'yes':
                    completed['cleaned_room'] = True
                    player.morality += 3
                    print(dedent(f"""
                        You cleaned the room which made you feel really good
                        There is nothing else to do in the room
                        Your morality is {player.morality}
                        """))
                    break
                elif action == 'no':
                    player.morality -= 1
                    print(dedent(f"""
                        Ha!
                        You left the room messy
                        For doing such an evil thing you lost a morality point
                        There is nothing else to do in the bedroom
                        Your morality is {player.morality}
                        """))
                    break
                else:
                    action = input(valid_choice)

            print("There is nothing else to do in the bedroom")
            action = input(prompt)

            while True:
                if action == 'j':
                    return 'cabin_main_room'

                elif action == 'h' or action == 'k' or action == 'l':
                    print("You can't go that way")
                    action = input(prompt)

                else:
                    action = input(valid_move)
class OutsideCabin(object):
    def enter(self):
        print(dedent("""
            It's a beautiful sunny day outside
            To your left is a river
            To your right is the woods
            Straight ahead is a village
             """))
        action = input(prompt)

        while True:
            if action == 'h':
                return 'river'
            elif action == 'j':
                return 'cabin_main_room'
            elif action == 'k':
                return 'village'
            elif action == 'l':
                return 'woods'
            else:
                action = input(valid_move)

class River(object):
    def enter(self):
        if completed['kid_drowning'] == False:
            print(dedent("""
                Upon approaching the river you see a kid drowning
                He's screaming for help
                You have two options
                Type yes to save the kid from drowning
                Type no to pretend like you didn't see him and return to outside the cabin
                """))
            action = input(prompt)

            while True:
                if action == 'yes':
                    completed['kid_drowning'] = True
                    player.morality += 10
                    print(dedent(f"""
                        You found some rope next to you and tossed an end to the kid
                        You managed to pull him in and save his life
                        He runs away thanking you
                        This gave you 10 points of mortality
                        Your morality is {player.morality}
                        """))
                    break
                elif action == 'no':
                    completed['kid_drowning'] = True
                    player.morality -= 10
                    print(dedent(f"""
                        You casually just turn around and walk back to outside the cabin
                        After a little while the kid stops screaming for help
                        Shockingly you lose 10 points of morality
                        Your morality is {player.morality}
                        """))
                    return 'outside_cabin'
                else:
                    action = input(valid_choice)

        print("There is nothing to do here anymore")
        action = input(prompt)

        while True:
            if action == 'j':
                return 'outside_cabin'

            elif action == 'h' or action == 'k' or action == 'l':
                print("You can't go that way")
                action = input(prompt)

            else:
                action = input(valid_move)
