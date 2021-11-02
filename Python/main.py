import udvozles_kiiro
import menu_kiiro
import fajlbeolvasas

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
                print("bbbb")
                break
            elif answer == 'c':
                print("cccc")
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
