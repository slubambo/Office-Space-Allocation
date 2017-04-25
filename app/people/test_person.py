import unittest
from .person import Person
from .person import Staff


class PersonTests(unittest.TestCase):

    # Test methods in class Room

    def test_create_person(self):

        result = Person.create_person(Staff, "Simon", "Fred")

        self.assertEqual("You have added Simon Fred!", result,
                         msg='Should person Simon Fred')

        self.assertEqual(len(Person.people), 1)
        self.assertEqual(len(Person.allStaff), 1)
