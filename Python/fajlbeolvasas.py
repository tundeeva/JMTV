import festmenyek_class

class Beolvasas:

def __init__(self):
    
    fajl = input("Kérem a fájl nevét: ")
    inputFile(fajl, rekordok)
    print("\tA fájl beolvasása ... kész!")

    for i in range(len(rekordok)):
        print("\t"+rekordok[i].toString())
return
        
    

def inputFile(self, file, lista):
f = open(file, "r", encoding='utf-8')

rekordok[:] = []
    
for sor in f:
    sor=sor[:-1].split(";")
    peldany = festmenyek_class.Festmenyek(sor[0],sor[1],sor[2])
    lista.append(peldany)
f.close()
return


