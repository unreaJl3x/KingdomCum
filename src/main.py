from chapterTwo import *
from chapterOne import *
#from chapterThree import *


def randfomNameConsole():
    titles = ["Я атменил тп","На нахимове нет людей","Потные мужчины тягают железо,"
        " Вот так в нашем зале качаются к лету","Дорогой дневник, мне не подобрать слов, чтобы описать боль и унижение, которое я испытал.",
    "Ты и ДжоДжо уже целовались? Ещё нет, так ведь? Твой первый поцелуй принадлежит не ему! Это был я, Дио!",
              "Я РУССКИЙ!!!",
              "Здравствуйте. Это Я. СТУЛ АЛЕКСЕЯ НАВАЛЬНОГО!",
              "Владимир Путин молодец"]
    os.system("title "+titles[random.randint(0,len(titles)-1)])

def logo():
    print(""" 
____  __.__                   .___             _________                
|    |/ _|__| ____    ____   __| _/____   _____ \_   ___ \ __ __  _____  
|      < |  |/    \  / ___\ / __ |/  _ \ /     \/    \  \/|  |  \/     \ 
|    |  \|  |   |  \/ /_/  > /_/ (  <_> )  Y Y  \     \___|  |  /  Y Y  \\
|____|__ \__|___|  /\___  /\____ |\____/|__|_|  /\______  /____/|__|_|  /
        \/       \//_____/      \/            \/        \/            \/ 
""")

def main():
    randfomNameConsole()
    os.system("cls")
    logo()
    print("Enter any key to start....\r",end="")
    input("\r")
    #os.system("cls")
    pl = Player("hui",0)
    pl.LevleUp(4)

    print("\r Chapter One\n Chapter Two\n Chapter Three")
    choice = input("Choice chapter")

    match choice:
        case "1":
            chapterOne(pl)
            chapterTwo_second(pl)
            # chapterThree(pl)

        case "2":
            chapterTwo_second(pl)
            # chapterThree(pl)

        #case 3:
            #chapterThree(pl)

main()