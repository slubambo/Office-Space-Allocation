from app.people.person import Person


class Fellow(Person):
    def __init__(self, name):
        super(Fellow, self).__init__(name, "Fellow")
        self.living_space = ""
