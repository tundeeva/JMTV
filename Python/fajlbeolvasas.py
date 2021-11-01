import festmenyek_class
rekordok = []

def f1(label):
    print(label)
    fajl = input("Kérem a fájl nevét: ")
    inputFile(fajl, rekordok)
    print("\tA fájl beolvasása ... kész!")

    for i in range(len(rekordok)):
        print("\t"+rekordok[i].toString())
        
    

def inputFile(file, lista):
    f = open(file, "r")

    rekordok[:] = []
    
    for sor in f:
        sor=sor[:-1].split(";")
        peldany = festmenyek_class.Festmenyek(sor[0],sor[1],sor[2])
        lista.append(peldany)
    f.close()
    return

f1("Festmény adatbázis")
