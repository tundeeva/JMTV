
class InputFile:
    def __init__(self, file, lista):
        f = open(file, "r")
        for sor in f:
            sor = sor[:-1].split(";")
            lista.append([str(sor[0]), int(sor[1]), str(sor[2])])
        f.close()
        return
        
class Search_cmd:
    '''Fő osztály'''
    festmeny_now = []   #most üres de később ez lesz a pillanatnyi!!
    festmeny_all = []   #összes eddigi festmeny.txt
    
    #Search_cmd.inputFile("festmeny_v.txt", festmeny_all)
    
    def __init__(self, label):
        print(label)
        
        '''Egy kicsi menü, amiben választani lehet majd egy pár opció közül'''
        
        self.m_1 = "\n\tNév keresése a kiválasztot listából" + "\t--\t1"
        print(self.m_1)
        self.m_2 = "\tNév keresése az összes listából\t" + "\t--\t2"
        print(self.m_2)
        txt = "\n\tKérlek válasz az opciók közül: "
        self.a = int(input(txt))
        
        # Ha függvény a választás megvalósításához
        
        if self.a == 1:
            for i in range(len(self.festmeny_all)):
                print(self.festmeny_all[i][0])
                
        elif self.a == 2:
            txt = "Sikeres keresés"
            print(txt)
            
        
# A modul inulásának parancsai
InputFile("festmeny_v.txt", Search_cmd.festmeny_all)
Search_cmd("\nÜdvözöllek a Névkeresőben!")
# A modul teszteléséhez szükséges
input("<<Enter>>")
