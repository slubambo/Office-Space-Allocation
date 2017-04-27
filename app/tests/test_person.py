import unittest

from app.dojo.dojo import Dojo


class PersonTests(unittest.TestCase):
    # Test methods in class Room

    def test_create_person_successfully(self):

        dojo_instance = Dojo()

        initial_people_count = len(dojo_instance.allPeople)
        new_staff = dojo_instance.create_person("staff", "Simon")
        self.assertTrue(new_staff)
        new_people_count = len(dojo_instance.allPeople)
        self.assertEqual(new_people_count - initial_people_count, 1)

    def test_create_person_with_many_names_successfully(self):

        dojo_instance = Dojo()
        initial_people_count = len(dojo_instance.allPeople)
        new_person = dojo_instance.create_person("fellow", "Simon" "Fred" "Y")
        self.assertTrue(new_person)
        new_people_count = len(dojo_instance.allPeople)
        self.assertEqual(new_people_count - initial_people_count, 1)
