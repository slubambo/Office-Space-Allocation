import unittest
from .room import Room


class RoomTests(unittest.TestCase):
    # Test methods in class Room

    def test_single_room_creation(self):

        result = Room.create_room("Office", "Mandela")

        self.assertEqual("You have created a new office called Mandela!", result,
                         msg='Should create Office called Mandela')

    def test_other_room_not_office_nor_livingSpace(self):

        result = Room.create_room("Pantry", "Mandela")

        self.assertEqual("You can only create rooms of type Office or Living Space", result,
                         msg='Rooms can either be of type Office or Living Space')

    def test_multiple_rooms_creation(self):
        self.assertEqual(Room.create_room(self, "Office", "Mandela", "Angola", "Nigeria", "Ghana", "Nairobi"),
                         "You have created the following offices: \n Mandela \n Angola \n Nigeria \n Ghana \n Nairobi")

    def test_type_other_variables_other_than_string(self):

        result = Room.create_room(1, "Mandela")

        self.assertEqual("Room type is a string: Office or LivingSpace", result,
                         msg='Enter room type as a string: Office or Living Space')

    def test_name_other_variables_other_than_string(self):

        result = Room.create_room("Office", True)

        self.assertEqual("Room name can only be a string", result,
                         msg='Enter room name as a string eg. Orange')

    def test_class_room(self):

        room_instance = Room()
        sample_office = Room.create_room("Office", "sampleOffice")
        sample_living_space = Room.create_room("Living Space", "sampleLivingSpace")

        total_rooms = Room.allRooms
        total_offices = Room.allOffices
        total_living_spaces = Room.allLivingRooms

        self.assertEqual(len(total_rooms), 2)
        self.assertEqual(len(total_offices), 1)
        self.assertEqual(len(total_living_spaces), 1)


if __name__ == '__main__':
    unittest.main()
