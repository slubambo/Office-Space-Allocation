from __future__ import with_statement

from app.people.staff import Staff
from app.people.fellow import Fellow
from app.rooms.office import Office
from app.rooms.living_space import LivingSpace

from app.helpers import general_helper

import random
import sys


class Dojo(object):
    def __init__(self):

        self.allPeople = []
        self.allStaff = []
        self.allFellows = []

        self.allRooms = []
        self.allOffices = []
        self.allLivingRooms = []

        self.assignedRooms = []
        self.assignedLivingRooms = []
        self.assignedOffices = []

    def create_person(self, person_type, *args):

        if len(args) >= 1 and all(isinstance(item, str) for item in args):

            if person_type.lower() == "staff":
                staff = Staff(" ".join(str(x) for x in args))
                self.allPeople.append(staff)
                self.allStaff.append(staff)

                return staff

            if person_type.lower() == "fellow":
                fellow = Fellow(" ".join(str(x) for x in args))
                self.allPeople.append(fellow)
                self.allFellows.append(fellow)

                return fellow
        else:
            return "At least one name is needed and all names must be strings"

    def create_room(self, args):
        return_message = []
        if len(args) >= 2 and all(isinstance(item, str) for item in args):

            room_type = args[0]

            # checking if room type is Office or living space and if the office is a string

            if isinstance(room_type, str) and (room_type.lower() == "office" or room_type.lower() == "living space"):

                if len(args) == 2:

                    room_name = args[1]

                    if room_type == "office":

                        new_office = Office(room_name)

                        if new_office not in self.allRooms:
                            self.allOffices.append(new_office)
                            self.allRooms.append(new_office)
                        else:
                            return_message.append(new_office.name + " already exits \n")

                        return return_message
                    else:
                        new_living_space = LivingSpace(room_name)

                        if new_living_space not in self.allRooms:
                            self.allLivingRooms.append(new_living_space)
                            self.allRooms.append(new_living_space)

                        return return_message

                elif len(args) > 2:

                    new_list = general_helper.remove_list_duplicates(args[1:])

                    for name in new_list:
                        if name not in self.allRooms:
                            if room_type == "office":
                                new_office = Office(name)

                                if new_office not in self.allRooms:
                                    self.allOffices.append(new_office)
                                    self.allRooms.append(new_office)
                                else:
                                    return_message.append(new_office.name + " already exits \n")

                            else:
                                new_living_space = LivingSpace(name)

                                if new_living_space not in self.allRooms:
                                    self.allLivingRooms.append(new_living_space)
                                    self.allRooms.append(new_living_space)
                                else:
                                    return_message.append(new_office.name + " already exits \n")
                        else:
                            pass

                    return self

                else:
                    return None

            else:
                return "Wrong office type or Wrong Data type for Office!"
        else:
            return "Input must contain the room type, at-least one room name and all inputs must be strings"

    def get_available_rooms(self, room_type):
        if not isinstance(room_type, str):
            raise ValueError('Room type must be passed as a list.')

        if len(self.allRooms) <= 0:
            return "No rooms available!"
        else:
            available_rooms = []

            if room_type == "office" and self.allOffices:

                for room in self.allOffices:
                    if room.occupants < room.capacity:
                        available_rooms.append(room)

            elif room_type == "living space" and self.allLivingRooms:
                for room in self.allLivingRooms:
                    if room.occupants < room.capacity:
                        available_rooms.append(room)
            else:
                pass

            return available_rooms

    def assign_room(self, person_type, person_object, needs_living_space=False):

        if len(self.allRooms) <= 0:

            print("No Rooms available")
            return "No Rooms available"

        else:
            # first assign office
            if len(self.allOffices) <= 0:
                print("No Office Space available")
                return "No Office Space available"

            else:

                if person_object.office == "":

                    # picking available rooms
                    available_offices = self.get_available_rooms("office")

                    if len(available_offices) >= 1:

                        office_to_assign = random.choice(available_offices)
                        person_object.office = office_to_assign.name

                        office_to_assign.occupants += 1

                        self.assignedOffices.append(office_to_assign)
                        self.assignedRooms.append(office_to_assign)

                    else:
                        print("No available offices found")
                else:
                    print("Already has office")

            # then allocating Living room depending on person type

            if person_type == "fellow" and needs_living_space:

                available_living_rooms = self.get_available_rooms("living space")

                if len(available_living_rooms) >= 1:

                    living_space_to_assign = random.choice(available_living_rooms)

                    person_object.LivingSpace = living_space_to_assign.name

                    living_space_to_assign.occupants += 1

                    self.assignedLivingRooms.append(living_space_to_assign)

                    self.assignedRooms.append(living_space_to_assign)

                else:

                    print("No available Living rooms found")

        return self

    def add_person(self, *args):
        if len(args) >= 3:
            # Let us split list to separate concerns accommodation

            wants_accommodation = args[-1]

            person_type = args[-2]

            person_names = args[:-2]

            # first we create the person

            if len(person_names) >= 1 and ( person_type.lower() == "staff" or person_type.lower() == "fellow"):

                # creating staff and assigning office
                if person_type.lower() == "staff":

                    staff_created = self.create_person("staff", *person_names)

                    # now assign office

                    self.assign_room("staff", staff_created, False)

                else:

                    fellow_created = self.create_person("fellow", *person_names)

                    if wants_accommodation.lower() == "y" or wants_accommodation.lower() == "yes":
                        self.assign_room("fellow", fellow_created, True)
                    else:
                        self.assign_room("fellow", fellow_created, False)

                print(self.assignedLivingRooms)

                return self
            else:
                print("Either no names were added or a wrong person type is entered")
                return "Either no names were added or a wrong person type is entered"

        else:
            print("List input must include at least 3 items (names, person type and if they want accommodation")
            return "List input must include at least 3 items (names, person type and if they want accommodation"

    def print_room(self, room_name):

        if not isinstance(room_name, str):
            raise ValueError('Room type must be passed as a string.')

        if general_helper.binary_search_if_item_in_list(self.allRooms, room_name):

            list_of_people_in_room = []

            # find if people are assigned this room
            for person_to_check in self.allPeople:

                # checking offices
                if person_to_check.office.lower() == room_name.lower():
                    list_of_people_in_room.append(person_to_check.name)

                # checking Living Spaces
                if person_to_check.person_type == "Fellow" and person_to_check.LivingSpace.lower() == room_name.lower():
                    list_of_people_in_room.append(person_to_check.name)


            if len(list_of_people_in_room) >= 1:

                print(list_of_people_in_room)
                return list_of_people_in_room

            else:
                return "No People found in this room"
        else:
            return "Room not found"

        return None

    def print_allocations(self, filename=None):

        if len(self.allRooms) <= 0:
            return "No Rooms found"

        # No file required so we print normally
        if filename is None:

            for room in self.allRooms:

                print("\n")

                print(room.name + "     (" + room.room_type + ")")

                print("_"*40)

                print("")

                list_of_people_assigned = self.return_list_of_people_in_room(room.name)

                if isinstance(list_of_people_assigned, list):

                    print(', '.join(map(str, list_of_people_assigned)))
                    print("\n")

                else:
                   print("No People assigned to this room")
                   print("\n")

            return True

        elif isinstance(filename, str):

            file_to_print = open("resources/"+filename+".txt", "w")

            for room in self.allRooms:

                file_to_print.write("\n")
                file_to_print.write(room.name + "     (" + room.room_type + ")")

                file_to_print.write("\n")
                file_to_print.write("_"*40)
                file_to_print.write("\n")

                list_of_people_assigned = self.return_list_of_people_in_room(room.name)

                if isinstance(list_of_people_assigned, list):

                    file_to_print.write(', '.join(map(str, list_of_people_assigned)))
                    file_to_print.write("\n")

                else:
                    file_to_print.write("No People assigned to this room")
                    file_to_print.write("\n")

            file_to_print.close()

            return True

        else:

            return None

    # function that simply returns a list of names. It is almost similar to the function of print_room
    def return_list_of_people_in_room(self, room_name):

        list_of_people_in_room = []

        # find if people are assigned this room
        for person_to_check in self.allPeople:

            # checking offices
            if person_to_check.office.lower() == room_name.lower():
                list_of_people_in_room.append(person_to_check.name)

            # checking Living Spaces
            if person_to_check.person_type.lower() == "fellow":
                if person_to_check.LivingSpace == room_name:
                    list_of_people_in_room.append(person_to_check.name)

        if len(list_of_people_in_room) >= 0:

            return list_of_people_in_room


