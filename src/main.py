import random
import os
from player import *
from Messenger import * # каждый круг будет проверять сообщения. через него будем хуярить глобальные по типу описания пещер наверное?
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
    pl = Player('Player', 0)

    sceneTest = Scene(5,3)
    sceneTest.Insert(pl.char, Point(0,0),pl)
    enemy = Person("Abramov",1,10,char='e')
    sceneTest.Insert(enemy.char, Point(3,0),enemy,True)

    enemy.inter.AddInteraction(Interact("say","I am rockstar",False))

    while(True):
        sceneTest.PrintMap()
        #if sceneTest.GetPlayer().state == 0 :
        sceneTest.PlController()
        time.sleep(0.1)

main()