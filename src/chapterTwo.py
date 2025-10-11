import random
import os
from Scene.SceneController import *
from Scene.map import *
from Scene.Person.Inventory import *
from Scene.bot import *
import time

def Door(currentScene:Scene, newScene:Scene):
    pl = currentScene.GetPlayer()
    currentScene = newScene
    currentScene.Insert(pl.char,Point(0,0),obj=pl)

def chapterTwo_second(pl:Player):
    mainScene = Scene()

    sceneLobby = Scene(5, 3)
    sceneLobby.Insert(char="p", p=Point(0, 0), obj=pl)
    butler = Person(name="Дворецкий",race=0,aggresive=2)
    butler.inter.AddInteraction(Interact("say"," “Ваше высочество, вас сегодня ждет встреча с "+colored("3 послами из разных стран","cyan")+", они прибыли из Амидонии, Контареллы и Сархана и уже ожидают вас в тронном зале.\n"))

    doorLobby = Entity(name="Door to troneHall.",char='dtr')
    doorLobby.inter.AddInteraction(Interact("open","Do you want teleport to TrhoneHall?(y/a)", func=Door, params=list[mainScene,sceneLobby]))
    sceneLobby.Insert(doorLobby.char,Point(4,0),obj=doorLobby,canInter=True,collision=True)
    print(
"От войны не осталось и следа, здания были отреставрированы, улицы убраны, а люди спешили на работу.\n"+
"Находясь в своем новом дворце, принц был очень доволен результатом.\n"
"Стоявший рядом дворецкий, увидел довольное лицо и в его груди что-то защемило, но он резко откинул все внутри себя и холодным голосом сказал принцу: \n\n")
    input(".....")

    mainScene = sceneLobby
    while (True):
        if pl.health <= 0:
            print("Game Over")
            return

        if mainScene.GetPlayer().state == 0:
            mainScene.PrintMap()
            mainScene.PlController()

        elif mainScene.GetPlayer().state == 1:
            action_pl = mainScene.PlFight()
            action_bot = FightBot(pl, mainScene.enemyFight)
            print(action_bot)
            mainScene.FightAction(action_bot, pl, mainScene.enemyFight)
            input()
            mainScene.FightAction(action_pl, mainScene.enemyFight, pl)
            input()

        time.sleep(0.1)
        os.system("cls")