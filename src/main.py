import random
import os
from Scene.SceneController import *
from Scene.map import *
from Scene.Person.Inventory import *
from Scene.bot import *
from chapterTwo import *
import time

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
    input("Enter any key to start....")
    os.system("cls")
    pl = Player("hui",0)
    chapterTwo_second(pl)

main()