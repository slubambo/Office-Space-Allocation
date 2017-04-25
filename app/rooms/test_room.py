import unittest
from .room import Room


class RoomTests(unittest.TestCase):

    def test_create_room_successfully(self):
        my_class_instance = Room()
        initial_room_count = len(my_class_instance.allRooms)
        blue_office = my_class_instance.create_room("office", "Blue")
        self.assertTrue(blue_office)
        new_room_count = len(my_class_instance.allRooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_multiple_rooms_successfully(self):
        my_room_instance = Room()
        initial_room_count = len(my_room_instance.allRooms)
        new_offices = my_room_instance.create_room("office", "Blue", "Orange", "Green", "Cream", "Mandela")
        self.assertTrue(new_offices)
        new_room_count = len(my_room_instance.allRooms)
        self.assertEqual(new_room_count - initial_room_count, 5)

    def test_create_unknown_office_type(self):
        my_room_instance = Room()

        result = my_room_instance.create_room("Pantry", "Blue", "Orange")

        self.assertEqual("Wrong office type or Wrong Data type for Office!", result,
                         msg='Office types are Office and Living room only')

    def test_create_wrong_office_type_data_type(self):
        my_room_instance = Room()

        result = my_room_instance.create_room(1, "Blue", "Orange")

        self.assertEqual("Input must contain the room type, at-least one room name and all inputs must be strings", result,
                         msg='Office types are Office and Living room only')

    def test_create_wrong_office_name_data_type(self):
        my_room_instance = Room()

        result = my_room_instance.create_room("Office", "Blue", 1, "Green", True, "Purple")

        self.assertEqual("Input must contain the room type, at-least one room name and all inputs must be strings", result,
                         msg='Office names can only be strings')


if __name__ == '__main__':
    unittest.main()
