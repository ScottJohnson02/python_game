# Rooms
from sys import exit
from random import randint
from textwrap import dedent
from player_stats import *
prompt = "~> "
# have classes pass through a parent to check if they can be entered

completed = {
        'drugs': False,
        'cleaned_room': False,
        'kid_drowning': False,
        'cannibals': False
        }

class InitialRoom(object):
    def __init__(self):
        self.directions = []
    def dir(self):
        while True:
            action = input('~> ')
            if action == 'help':
                print(dedent("""
                    If at any point you are unsure of all available actions just type help
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
                    """))
                action = self.dir()
            if action in self.directions:
                return action
            else:
                print("Not a valid action right now")

class Introduction(InitialRoom):
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
        self.directions = ['k']
        action = self.dir()

        if action == 'k':
            print("The door you came out of slammed shut behind you and disappeared")
            return 'cabin_main_room'


class CabinMainRoom(InitialRoom):
    def enter(self):
        print(dedent("""
            You are standing in the entrance of a cabin
            To your right there is a bathroom
            Behind you is a bedroom
            In front of you is a door to leave the cabin
            """))
        self.directions = ['k', 'l', 'j']
        action = self.dir()

        if action == 'k':
            return 'outside_cabin'
        elif action == 'l':
            return 'cabin_bathroom'
        elif action == 'j':
            return 'cabin_bedroom'


class CabinBathroom(InitialRoom):
    
    def enter(self):
        if completed['drugs'] == False:
            self.directions = ['yes', 'no']
            print(dedent("""
                There is a pill in the bathroom that is only precribed to people with cancer
                You don't have cancer
                Taking it will get you really high
                Do you take it?
                Taking it will decrease your morality by 5
                """))
            action = self.dir()

            if action == 'yes':
                completed['drugs'] = True
                player.morality -= 5
                print(dedent("""
                    After taking the pill your whole body feels amazing
                    There is nothing else in the bathroom to use
                    Your morality is {player.morality}
                    """))

            elif action == 'no':
                print(dedent(f"""
                    You refrained from stealing drugs
                    Your morality is {player.morality}
                    """))
    
        self.directions = ['j']
        print(dedent("""
            There is nothing else in the bathroom to use
            All you can do is head back
            """))

        action = self.dir()
        if action == 'j':
            return 'cabin_main_room'


class CabinBedroom(InitialRoom):

    def enter(self):
        if completed['cleaned_room'] == False:
            self.directions = ['yes', 'no']
            print(dedent("""
                The bedroom is messy
                Do you clean it?
                Cleaning the bedroom will increase your morality by 3
                """))
            action = self.dir()

            if action == 'yes':
                completed['cleaned_room'] = True
                player.morality += 3
                print(dedent(f"""
                    You cleaned the room which made you feel really good
                    There is nothing else to do in the room
                    Your morality is {player.morality}
                    """))
            elif action == 'no':
                player.morality -= 1
                print(dedent(f"""
                    Ha!
                    You left the room messy
                    For doing such an evil thing you lost a morality point
                    There is nothing else to do in the bedroom
                    Your morality is {player.morality}
                    """))

        self.directions = ['j']
        print("There is nothing else to do in the bedroom")
        action = self.dir()

        if action == 'j':
            return 'cabin_main_room'


class OutsideCabin(InitialRoom):
    def enter(self):
        print(dedent("""
            It's a beautiful sunny day outside
            To your left is a river
            To your right is the woods
            Straight ahead is a village
             """))
        self.directions = ['h', 'j', 'k', 'l']
        action = self.dir()

        if action == 'h':
            return 'river'
        elif action == 'j':
            return 'cabin_main_room'
        elif action == 'k':
            return 'village'
        elif action == 'l':
            return 'woods'


class Woods(InitialRoom):
    def enter(self):
        if completed['cannibals'] == False:
            print(dedent("""
                You came upon a tribe of cannibals
                Rather than eat you they want to see if you'll eat human meat
                Eating the meat will decrease your morality by 5
                Do you eat it?
                """))
            self.directions = ['yes', 'no']
            action = self.dir()
            if action == 'yes':
                completed['cannibals'] = True
                player.morality -= 5
                print(dedent(f"""
                    You ate the meat and feel full
                    your new morality is {player.morality}
                    They thank you for eating with them and you head back
                    """))
                return 'outside_cabin'
            elif action == 'no':
                print(dedent("""
                    You screamed like a little girl and ran away from them
                    """))
                return 'outside_cabin'
        print(dedent("""
            You come back to the cannibal tribe and say hello to your friends
            The only direction to go is back
            """))
        self.directions = ['j']
        action = self.dir()
        if action == 'j':
            return 'outside_cabin'

class River(InitialRoom):
    def enter(self):
        if completed['kid_drowning'] == False:
            self.directions = ['yes', 'no']
            print(dedent("""
                Upon approaching the river you see a kid drowning
                He's screaming for help
                You have two options
                Type yes to save the kid from drowning
                Type no to pretend like you didn't see him and return to outside the cabin
                """))
            action = self.dir()

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

        self.directions = ['j']
        print("There is nothing to do here anymore")
        action = self.dir()

        if action == 'j':
            return 'outside_cabin'


class Village(InitialRoom):
    def enter(self):
        print(dedent("""
            You enter the village and there's lots of people walking around
            To your left is a brothel
            To your right is an animal rescue center
            In front of you is more of the village
            """))
        self.directions = ['h', 'l', 'j', 'k']
        action = self.dir()

        if action == 'h':
            print(dedent(f"""
                Woah there sonny!
                You need a morality score of -50 to enter here
                You currently have {player.morality}
                """))
            return 'village'
        elif action == 'l':
            print(dedent("""
                You need a morality score of 50 to enter here
                You currently have {player.morality}
                """))
            return 'village'
        elif action == 'k':
            print(dedent("""
            Still needs developed
            """))
            return 'village'
        elif action == 'j':
            return 'outside_cabin'
