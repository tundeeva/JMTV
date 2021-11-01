import udvozles_class
import fomenu
import fajlbeolvasas

rekordok = []

def foprogram():
    udvozles_class.Udvozles()
    answer = ""
    while 1:
        fomenu.Fomenu()
        prompt = ">"
        while answer != ('a' or 'b' or 'c' or 'd' or 'e' or 'f' or 'exit'):
            answer = input(prompt)
        if answer == 'a':
            fajlbeolvasas.Beolvasas(rekordok)
    



foprogram()
