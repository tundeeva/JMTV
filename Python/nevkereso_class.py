

class Search:
    '''Fő osztály'''
    
    def menu(label):
        print(label)
        
        '''Egy kicsi menü, amiben választani lehet majd egy pár opció közül'''
        
        m_1 = "\n\tNév keresése a kiválasztot listából" + "\t--\t1"
        print(m_1)
        m_2 = "\tNév keresése az összes listából\t" + "\t--\t2"
        print(m_2)
        txt = "\n\tKérlek válasz az opciók közül: "
        a = int(input(txt))
        
        # Ha függvény a választás megvalósításához
        
        if a == 1:
            txt = "Sikeres keresés"
            print(txt)
        elif a == 2:
            txt = "Sikeres keresés"
            print(txt)
            
        
# A modul inulásának parancsa
Search.menu("\nÜdvözöllek a Névkeresőben!")
# A modul teszteléséhez szükséges
input("<<Enter>>")
