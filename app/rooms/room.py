import sys

from app.rooms.dojo import Dojo


class Room(Dojo):
    def __init__(self):
        self.allOffices = []
        self.allLivingRooms = []
        self.allRooms = []

    def create_room(self, *args):

        if len(args) >= 2 and all(isinstance(item, str) for item in args):

            room_type = args[0]

            # checking if room type is Office or living space and if the office is a string

            if isinstance(room_type, str) and (room_type.lower() == "office" or room_type.lower() == "living space"):

                if len(args) == 2:

                    room_name = args[1]

                    self.allRooms.append(room_name)

                    if room_type == "office":
                        self.allOffices.append(room_name)
                    else:
                        self.allLivingRooms.append(room_name)

                    return self

                elif len(args) > 2:

                    room_names = args[0: len(args) - 1]

                    for name in room_names:
                        self.allRooms.append(name)

                    return self

                else:
                    return None

            else:
                return "Wrong office type or Wrong Data type for Office!"
        else:
            return "Input must contain the room type, at-least one room name and all inputs must be strings"
