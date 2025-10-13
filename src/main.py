import os

from chapterTwo import *
from chapterOne import *
from chapterThree import *
from chapterFour import *

def randfomNameConsole():
    titles = ["Я атменил тп","На нахимове нет людей","Потные мужчины тягают железо,"
        " Вот так в нашем зале качаются к лету","Дорогой дневник, мне не подобрать слов, чтобы описать боль и унижение, которое я испытал.",
    "Ты и ДжоДжо уже целовались? Ещё нет, так ведь? Твой первый поцелуй принадлежит не ему! Это был я, Дио!",
              "Я РУССКИЙ!!!",
              "Здравствуйте. Это Я. СТУЛ АЛЕКСЕЯ НАВАЛЬНОГО!",
              "Владимир Путин молодец","Жужа или Крэкеры?"]
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
    print("Enter any key to start....",end="")
    input("")

    print("|     StoryMode     |")
    print("_____________________")
    print("\r Chapter One\n Chapter Two\n Chapter Three\n Chapter Four")
    choice = input("Choice chapter")

    pl = Player(input("Enter youre name... "), 0)
    pl.LevleUp(8)
    os.system("cls")
    match choice:
        case "1":
            chapterOne(pl)
            print("Спустя несколько месяцев.....")
            os.system("cls")
            chapterTwo_second(pl)
            os.system("cls")
            print("Из окна на них глядел дворецкий, явно недовольный, что принц заводит новые знакомства и наращивает мощь. Холодным взглядом, перед тем как уйти, он обводит “Хрустальную розу” и королеву Контареллы, и растворяясь в темноте")
            chapterThree(pl)
            chapterFour(pl)

        case "2":
            chapterTwo_second(pl)
            os.system("cls")
            print("Из окна на них глядел дворецкий, явно недовольный, что принц заводит новые знакомства и наращивает мощь. Холодным взглядом, перед тем как уйти, он обводит “Хрустальную розу” и королеву Контареллы, и растворяясь в темноте")
            chapterThree(pl)
            chapterFour(pl)
        case "3":
            chapterThree(pl)
            chapterFour(pl)
        case "4":
            chapterFour(pl)

main()
