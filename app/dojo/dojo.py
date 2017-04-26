from app.people.staff import Staff
from app.people.fellow import Fellow
from app.rooms.office import Office
from app.rooms.living_space import LivingSpace

from app.helpers import general_helper

import random


class Dojo(object):
    def __init__(self):
        self.allPeople = []
        self.allStaff = []
        self.allFellows = []

        self.allRooms = []
        self.allOffices = []
        self.allLivingRooms = []

        self.assignedRooms = []

    # <editor-fold desc="This region is for methods that deal with person">
    def create_person(self, person_type, *args):

        if len(args) >= 1 and all(isinstance(item, str) for item in args):

            if person_type.lower() == "staff":
                staff = Staff(" ".join(str(x) for x in args))
                self.allPeople.append(staff)
                self.allStaff.append(staff)

                return staff
            else:
                fellow = Fellow(" ".join(str(x) for x in args))
                self.allPeople.append(fellow)
                self.allFellows.append(fellow)

                return fellow
        else:
            return "At least one name is needed and all names must be strings"

    def get_available_rooms(self, room_type):
        if not isinstance(room_type, str):
            raise ValueError('Room type must be passed as a list.')

        if len(self.allRooms) <= 0:
            return "No rooms available!"
        else:
            available_rooms = []

            for room in self.allRooms:
                if room.occupants < room.capacity:
                    available_rooms.append(room)

            return available_rooms

    def assign_room(self, person_type, person_object, needs_living_space=False):
        if len(self.allRooms) <= 0:

            print("No Rooms available")
            return "No Rooms available"

        else:
            # first assign office office
            if len(self.allOffices) <= 0:
                print("No Office Space available")
                return "No Office Space available"
            else:
                if person_object.office == "":
                    available_offices = self.get_available_rooms("office")
                    if len(available_offices) >= 1:
                        
                        office_to_assign = random.choice(available_offices)
                        person_object.office = office_to_assign.name

                        office_to_assign.occupants += 1
                        self.assignedRooms.append(office_to_assign)

                        return self
                    else:
                        print("No available offices found")
                else:
                    print("Already has office")



                # </editor-fold>

                # <editor-fold desc="This region contains methods that deal with room">

    def create_room(self, *args):

        if len(args) >= 2 and all(isinstance(item, str) for item in args):

            room_type = args[0]

            # checking if room type is Office or living space and if the office is a string

            if isinstance(room_type, str) and (room_type.lower() == "office" or room_type.lower() == "living space"):

                if len(args) == 2:

                    room_name = args[1]

                    if room_type == "office":
                        new_office = Office(room_name)

                        self.allOffices.append(new_office)
                        self.allRooms.append(new_office)
                    else:
                        new_living_space = LivingSpace(room_name)

                        self.allLivingRooms.append(new_living_space)
                        self.allRooms.append(new_living_space)
                    return self

                elif len(args) > 2:

                    new_list = general_helper.remove_list_duplicates(args[1:])

                    for name in new_list:
                        if name not in self.allRooms:
                            if room_type == "office":
                                new_office = Office(name)

                                self.allOffices.append(new_office)
                                self.allRooms.append(new_office)
                            else:
                                new_living_space = LivingSpace(name)

                                self.allLivingRooms.append(new_living_space)
                                self.allRooms.append(new_living_space)
                        else:
                            pass

                    return self

                else:
                    return None

            else:
                return "Wrong office type or Wrong Data type for Office!"
        else:
            return "Input must contain the room type, at-least one room name and all inputs must be strings"

# </editor-fold>
