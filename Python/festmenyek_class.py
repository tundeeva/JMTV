class Festmenyek:
    def __init__(self, cim, ertek, stilus):
        self.cim = cim
        self.ertek = int(ertek)
        self.stilus = stilus

    def toString(self):
        txt ="\t"+ self.cim + ";"+ str(self.ertek)+ " Ft" + ";"+self.stilus
        return txt









