from app.rooms.room import Room


class LivingSpace(Room):
    def __init__(self, name):
        super(LivingSpace, self).__init__(name, "Living Space", 4)