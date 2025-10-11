import random
import os
from Scene.SceneController import *
from Scene.map import *
from Scene.bot import *
import time

def setMap(param):
    if input() != "y":
        print("Долбаеб")
        return
    print("Съебался")
    l = []
    for i in param:
        l.append(i)
    l[0].map = l[1]
    pGet = l[0].map.Find(char=l[2].char)
    if (len(pGet)<2):
        l[0].Insert(l[2].char, l[3], obj=l[2])

def chapterTwo_second(pl:Player):
    scene = Scene(5,3)

    #SPRTES________________________________
    scene.AddSprite(Sprite("poslanets",["|||||","|0-0|","|||||"]))
    scene.AddSprite(Sprite("d",["|---|","| + |","|___|"]))
    scene.AddSprite(Sprite("b",["-----","  0_0"," _||_"]))

    lobbyMap = Map(5,3)
    throneHallMap = Map(7, 4)

    #LOBBY_________________________________________
    lobbyMap.Insert(pl.char, Point(0,0),pl)
    butler = Person("player",0,0,'b')
    butler.inter.AddInteraction(Interact("say", "“Ваше высочество, вас сегодня ждет встреча с "+colored("3 послами из разных стран","cyan")+", они прибыли из Амидонии, Контареллы и Сархана. Они уже ожидают вас в тронном зале."))
    door = Person("door", 0, 0,'d')
    door.inter.AddInteraction(Interact(f"teleport", "This door lead to "+colored("ThroneHall","yellow")+". Do you want пойти нахуй(y/n): ", False, setMap, scene, throneHallMap, pl,Point(1,0)))
    lobbyMap.Insert(butler.char, Point(7,0),butler,True,True)
    lobbyMap.Insert(door.char, Point(4,0),door,True,True)

    #THRONE________________________________________
    doorToLobby = Person("door", 0, 0,'d')
    doorToLobby.inter.AddInteraction(Interact(f"teleport", "This door lead to "+colored("Lobby","yellow")+". Do you want пойти нахуй(y/n): ", False, setMap, scene, lobbyMap, pl))
    throneHallMap.Insert(doorToLobby.char, Point(0,0),doorToLobby,True,True)

    poslanets = [Person("Иларион",0,0,char="poslanets"),
                 Person("Стосеул",0,0,char="poslanets"),
                 Person("Артанис V",0,0,char="poslanets")
    ]
    poslanets[0].inter.AddInteraction(Interact("say","“Приветствую вас ваше высочество, меня зовут Иларион, я представитель страны Сархана. Я бы хотел обсудить с вами два вопроса”"))

    for i in range(len(poslanets)):
        throneHallMap.Insert(poslanets[i].char, Point(5,i+1),poslanets[i],True,True)

    print("От войны не осталось и следа, здания были отреставрированы, улицы убраны, а люди спешили на работу.\n"+"Находясь в своем новом дворце, принц был очень доволен результатом.\n""Стоявший рядом дворецкий, увидел довольное лицо и в его груди что-то защемило, но он резко откинул все внутри себя и холодным голосом сказал принцу: \n\n")
    input(".....")

    scene.map = lobbyMap
    os.system("cls")
    while (True):
        if pl.health <= 0:
            print("Game Over")
            return

        if scene.GetPlayer().state == 0:
            scene.PrintMap()
            scene.PlController()

        elif scene.GetPlayer().state == 1:
            action_pl = scene.PlFight()
            action_bot = FightBot(pl, scene.enemyFight)
            print(action_bot)
            scene.FightAction(action_bot, pl, scene.enemyFight)
            input()
            scene.FightAction(action_pl, scene.enemyFight, pl)
            input()

        time.sleep(0.1)
        os.system("cls")