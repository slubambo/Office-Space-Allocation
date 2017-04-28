from app.people.person import Person


class Staff(Person):
    def __init__(self, name):
        super(Staff, self).__init__(name, "Staff")