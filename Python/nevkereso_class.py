

class InputFile:
    def __init__(self, file, lista):
        f = open(file, "r", encoding='utf-8')
        for sor in f:
            sor = sor[:-1].split(";")
            lista.append([str(sor[0]), int(sor[1]), str(sor[2])])
        f.close()
        return
        
class Search_cmd:
    '''Fő osztály'''
    festmeny_now = []   #most üres de később ez lesz a pillanatnyi!!
    festmeny_all = []   #összes eddigi festmeny.txt
    # proba= ["fás"]
    
    #Search_cmd.inputFile("festmeny_v.txt", festmeny_all)
    
    def __init__(self, label):
        print(label)
        
        '''Egy kicsi menü, amiben választani lehet majd egy pár opció közül'''
        # proba = self.festmeny_all[0]
        # print(self.proba)
        self.m_1 = "\n\t1.)\tNév keresése a kiválasztot listából"
        print(self.m_1)
        self.m_2 = "\t2.)\tNév keresése az összes listából\t"
        print(self.m_2)
        txt = "\n\tKérlek válasz az opciók közül: "
        self.a = int(input(txt))
        
        # Ha függvény a választás megvalósításához
        
        if self.a == 1:
            for i in range(len(self.festmeny_all)):
                txt = self.festmeny_all[i][0]
                print(txt)
                
        elif self.a == 2:
            txt = "Sikeres keresés"
            print(txt)
            
        
# A modul inulásának parancsai
InputFile("festmeny_v.txt", Search_cmd.festmeny_all)
InputFile("festmeny_m.txt", Search_cmd.festmeny_all)
#InputFile("festmeny_t.txt", Search_cmd.festmeny_all)
Search_cmd("\nÜdvözöllek a Névkeresőben!")
# A modul teszteléséhez szükséges
input("<<Enter>>")
