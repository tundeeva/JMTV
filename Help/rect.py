#Popovics János

import rect_class
rekordok = []

def f1(label):
    print(label)
    inputFile("rectangles.txt", rekordok)
    print("\tA fájl beolvasás ... kész!")
    for i in range(5):
        print("\t" + rekordok[i].toString())


def f2(label):
    print(label)
    prompt = "\tKérek egy azonosítót [rect1-rect94]: "
    s = input(prompt)
    for i in range(len(rekordok)):
        if s == rekordok[i].id:
            print("\t" + rekordok[i].toString())


def f3(label):
    print(label)
    for i in range(len(rekordok)):
        if rekordok[i].a < 37:
            print("\t" + rekordok[i].id)


def f4(label):
    print(label)
    v = []
    for i in range(len(rekordok)):
        v.append(rekordok[i].volume())
    for i in range(len(rekordok)):
        if max(v) == rekordok[i].volume():
            print("\t" + rekordok[i].id)



def inputFile(file, lista):
    f = open(file, "r")
    for sor in f:
        sor = sor[:-1].split(";")
        példány = rect_class.Rectangle(sor[0], sor[1], sor[2], sor[3])
        lista.append(példány)
    f.close()
    return


f1("Popovics János\n1. feladat: fájl beolvasás, az első öt elem kiírása")
f2("2. feladat: egy tetszőleges elem kiírása")
f3("3. feladat: azon téglatestek ID-je melyek 'a' éle kisebb, mint 37 cm")
f4("4. feladat: XXL legnagyobb térfogatú téglatest(ek) ID-je")
