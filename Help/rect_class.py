# Popovics János

class Rectangle:
    def __init__(self, id, a, b, c):
        self.id = id
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)

    def volume(self):
        return self.a * self.b * self.c

    def toString(self):
        text = self.id + ": " + str(self.a) + " * " + str(self.b) + " * " + str(self.c) + " =\t" + str(self.volume()) + " cm3"
        return text
