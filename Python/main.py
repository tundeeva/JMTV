import udvozles_kiiro
import menu_kiiro
import fajlbeolvasas
import festmeny_hozzaadas
import festmenyek_class
import fajl_kiiras

rekordok = []

def main():
    udvozles_kiiro.Udvozles()
    answer = ""
    while 1:
        menu_kiiro.Fomenu()
        prompt = ">"
        while answer != 'exit':
            answer = input(prompt)
            if answer == 'a':
                fajlbeolvasas.Beolvasas(rekordok)
                break
            elif answer == 'b':
                fajl_kiiras.Kiiras(rekordok)
                break
            elif answer == 'c':
                festmeny_hozzaadas.FestményHozzáadás()
                break
            elif answer == 'd':
                print("dddd")
                break
            elif answer == 'e':
                print("eeee")
                break
            elif answer == 'f':
                print("ffff")
                break
            elif answer == 'exit':
                quit()
            answer = ""
    



main()
