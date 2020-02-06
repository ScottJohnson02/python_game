# Python3 Game

from rooms import *
class Map(object):

    room_names = {
            'intro': Introduction(),
            'cabin_main_room': CabinMainRoom(),
            'cabin_bathroom': CabinBathroom(),
            'cabin_bedroom': CabinBedroom(),
            'outside_cabin': OutsideCabin(),
            'river': River()
            }


    def __init__(self, start_room):
        self.start_room = start_room

    def next_room(self, room_name):
        val = Map.room_names.get(room_name)
        return val
    
    def opening_room(self):
        return self.next_room(self.start_room)
