# Python3 Game
import rooms


class Map(object):

    room_names = {
            'intro': rooms.Introduction(),
            'cabin_main_room': rooms.CabinMainRoom(),
            'cabin_bathroom': rooms.CabinBathroom(),
            'cabin_bedroom': rooms.CabinBedroom(),
            'outside_cabin': rooms.OutsideCabin(),
            'river': rooms.River(),
            'village': rooms.Village(),
            'woods': rooms.Woods()
            }

    def __init__(self, start_room):
        self.start_room = start_room

    def next_room(self, room_name):
        val = Map.room_names.get(room_name)
        return val
    
    def opening_room(self):
        return self.next_room(self.start_room)
