import random
import os
from player import *
from Scene.SceneController import Scene
from Scene.map import *
import time

def randfomNameConsole():
    titles = ["Я атменил тп","На нахимове нет людей","Потные мужчины тягают железо,"
        " Вот так в нашем зале качаются к лету","Дорогой дневник, мне не подобрать слов, чтобы описать боль и унижение, которое я испытал.",
    "Ты и ДжоДжо уже целовались? Ещё нет, так ведь? Твой первый поцелуй принадлежит не ему! Это был я, Дио!",
              "Я РУССКИЙ!!!",
              "Владимир Путин молодец"]
    os.system("title ",titles[random.randint(0,len(titles)-1)])

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
    #randfomNameConsole()
    logo()
    input("Enter any key to start....")
    #os.system("cls")

    sceneTest = Scene(5,3)
    enemy = Person("orc",0,10)
    sceneTest.map.Insert(enemy.char,Point(3,0),enemy,True)

    while(True):
        sceneTest.PrintMap()
        sceneTest.PlController()
        sceneTest.map.print()
        time.sleep(0.1)

main()


def zagadka(text:str, answer:str, errors:int) -> bool:
    print(text)
    for i in range(errors):
        if (input() == answer):
            return True
        print("lol")
    return False

##print(zagadka("24+3","27",3))