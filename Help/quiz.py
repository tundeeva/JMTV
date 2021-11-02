#Popovics János

import quiz_class
rekordok = []

def f1(label):
    print("Popovics János")
    print(label)
    inputFile("quiz.txt", rekordok)
    print("\tA fájl beolvasás ... kész!")
    print("\t" + rekordok[0].toString())
    print("\t" + rekordok[-1].toString())


def f2(label):
    print(label)
    prompt = "\tKérek egy csapatnevet: "
    s = input(prompt)
    for i in range(len(rekordok)):
        if s == rekordok[i].csapat:
            print("\t" + rekordok[i].toString())


def f3(label):
    print(label)
    for i in range(len(rekordok)):
        if rekordok[i].szumTTK() > rekordok[i].szumHUM():
            print("\t" + rekordok[i].csapat)


def f4(label):
    print(label)
    szumPontok, ttkPontok, humPontok = [], [], []
    for i in range(len(rekordok)):
        szumPontok.append(rekordok[i].szumPont())
        ttkPontok.append(rekordok[i].szumTTK())
        humPontok.append(rekordok[i].szumHUM())

    print("\tLegtöbb pontot elért csapatok:")
    for i in range(len(rekordok)):
        if rekordok[i].szumPont() == max(szumPontok):
            print("\t" + rekordok[i].csapat)

    print("\tLegtöbb TTK pontot elért csapatok:")
    for i in range(len(rekordok)):
        if rekordok[i].szumTTK() == max(ttkPontok):
            print("\t" + rekordok[i].csapat)

    print("\tLegtöbb HUM pontot elért csapatok:")
    for i in range(len(rekordok)):
        if rekordok[i].szumHUM() == max(humPontok):
            print("\t" + rekordok[i].csapat)


def inputFile(file, lista):
    f = open(file, "r")
    for sor in f:
        sor = sor[:-1].split(";")
        példány = quiz_class.Quiz(sor[0], sor[1], sor[2], sor[3], sor[4])
        lista.append(példány)
    f.close()
    return


f1("1. feladat: fájl beolvasás, az első és utolsó lista elem kiírása")
f2("2. feladat: egy tetszőleges csapat végeredményének kiírása")
f3("3. feladat: akiknek a ttk-s eredménye jobb mint a humán")
f4("4. feladat: XXL melyik csapat nyerte meg a versenyt, melyik a ttk-t és melyik a humánt")
