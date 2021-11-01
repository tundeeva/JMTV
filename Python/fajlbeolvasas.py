import festmenyek_class

class Beolvasas:

    def __init__(self, rekordok):
        self.rekordok = rekordok
        fajl = input("Kérem a fájl nevét: ")
        self.inputFile(fajl, self.rekordok)
        print("\tA fájl beolvasása ... kész!")

        return
        
    

    def inputFile(self, file, lista):
        f = open(file, "r", encoding='utf-8')

        self.rekordok[:] = []
    
        for sor in f:
            sor=sor[:-1].split(";")
            peldany = festmenyek_class.Festmenyek(sor[0],sor[1],sor[2])
            lista.append(peldany)
        f.close()
        return


