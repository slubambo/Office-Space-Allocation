#   This test file specifically tests methods that assign rooms, re-allocate and more

import unittest
from app.dojo.dojo import Dojo
from app.people.staff import Staff


class DojoTests(unittest.TestCase):
    def test_get_available_rooms(self):
        dojo_instance = Dojo()

        dojo_instance.create_room("office", "Blue")

        available_rooms = dojo_instance.get_available_rooms("office")
        self.assertTrue(available_rooms)

    def test_get_available_rooms_wrong_data_type_passed(self):
        dojo_instance = Dojo()
        self.assertRaises(ValueError, dojo_instance.get_available_rooms, 1)

    def test_get_available_rooms_when_no_rooms(self):
        dojo_instance = Dojo()

        available_rooms = dojo_instance.get_available_rooms("office")

        self.assertEqual("No rooms available!", available_rooms,
                         msg='No rooms available!')

    def test_assign_room_successfully(self):
        dojo_instance = Dojo()

        new_staff = dojo_instance.create_person("staff", "Simon")

        dojo_instance.create_room("office", "Blue")

        initial_assigned_room_count = len(dojo_instance.assignedRooms)

        assigned_office = dojo_instance.assign_room("staff", new_staff, False)

        self.assertTrue(assigned_office)

        new_assigned_room_count = len(dojo_instance.assignedRooms)

        self.assertEqual((initial_assigned_room_count + 1), new_assigned_room_count)

    def test_add_person_few_parameters(self):
        dojo_instance = Dojo()

        result = dojo_instance.add_person("Simon", "Fred")

        self.assertEqual("List input must include at least 3 items (names, person type and if they want accommodation",
                         result,
                         msg='List input must include at least 3 items (names, person type and if they want '
                             'accommodation')

    def test_add_person_wrong_person_types(self):
        dojo_instance = Dojo()

        result = dojo_instance.add_person("Simon", "Fred", "Green", "Y")

        self.assertEqual("Either no names were added or a wrong person type is entered", result,
                         msg='Either no names were added or a wrong person type is entered')

    def test_add_person_staff_successfully(self):
        dojo_instance = Dojo()
        dojo_instance.create_room("office", "Blue")
        dojo_instance.create_room("living space", "Yellow")
        initial_people_count = len(dojo_instance.allPeople)
        new_staff = dojo_instance.add_person("Simon", "Fred", "Lubambo", "staff", "N")
        self.assertTrue(new_staff)
        new_people_count = len(dojo_instance.allPeople)
        self.assertEqual((initial_people_count + 1), new_people_count)

    def test_add_person_fellow_successfully(self):
        dojo_instance = Dojo()
        dojo_instance.create_room("office", "Blue")
        dojo_instance.create_room("living space", "Yellow")
        initial_people_count = len(dojo_instance.allPeople)
        new_staff = dojo_instance.add_person("Simon", "Fred", "Lubambo", "fellow", "Y")
        self.assertTrue(new_staff)
        new_people_count = len(dojo_instance.allPeople)
        self.assertEqual((initial_people_count + 1), new_people_count)

if __name__ == '__main__':
    unittest.main()