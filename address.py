class Address:
    
    def __init__(self, index, city, street, build, room):
        self.index = index
        self.city = city
        self.street = street
        self.build = build
        self.room = room

    def __str__(self):
        return (f'{self.index}, {self.city}, {self.street}, {self.build}-{self.room}')