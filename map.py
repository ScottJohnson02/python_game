# Python3 Game

from rooms import *
class Map(object):

    room_names = {
            'intro': Introduction(),
            'cabin_main_room': CabinMainRoom(),
            'cabin_bathroom': Bathroom(),
            'cabin_bedroom': CabinBedroom()
            }


    def __init__(self, start_room):
        self.start_room = start_room

    def next_room(self, room_name):
        val = Map.room_names.get(room_name)
        return val
    
    def opening_room(self):
        return self.next_room(self.start_room)
