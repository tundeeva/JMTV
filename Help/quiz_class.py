#Popovics János

class Quiz:
    def __init__(self, csapat, ttk1, ttk2, hum1, hum2):
        self.csapat = csapat
        self.ttk1 = int(ttk1)
        self.ttk2 = int(ttk2)
        self.hum1 = int(hum1)
        self.hum2 = int(hum2)

    def szumPont(self):
        return self.szumTTK() + self.szumHUM()

    def toString(self):
        txt = self.csapat + ": " + str(self.szumPont()) + " pont"
        return txt

    def szumTTK(self):
        return self.ttk1 + self.ttk2

    def szumHUM(self):
        return self.hum1 + self.hum2
