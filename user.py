class User:

    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def sayFirst_Name (self):
        print (self.first_name)

    def sayLast_Name (self):
        print (self.last_name)

    def sayFull_Name (self):
        print (self.last_name, self.first_name)

