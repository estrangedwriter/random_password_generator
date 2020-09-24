import random

class algorithms:
    def __init__(self, listitems):
        self.listitems = listitems
        self.password = ""

    def shuffle(self, string):
        tempList = list(string)
        random.shuffle(tempList)
        return ''.join(tempList)

    def passwordGenerator(self):
        for i in range(0, int(self.listitems[0])):
            char = chr(random.randint(65,90))
            self.password = self.password + char

        for i in range(0, int(self.listitems[1])):
            char = chr(random.randint(97,122))
            self.password = self.password + char

        for i in range(0, int(self.listitems[2])):
            char = chr(random.randint(48,57))
            self.password = self.password + char

        for i in range(0, int(self.listitems[3])):
            char = chr(random.randint(33,43))
            self.password = self.password + char

        self.password = self.shuffle(self.password)
        self.shuffle(self.password)
        return self.password
    