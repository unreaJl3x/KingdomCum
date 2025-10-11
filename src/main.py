import random
import os
from Scene.SceneController import *
from Scene.map import *
from Scene.Person.Inventory import *
from Scene.bot import *
import time

def randfomNameConsole():
    titles = ["Я атменил тп","На нахимове нет людей","Потные мужчины тягают железо,"
        " Вот так в нашем зале качаются к лету","Дорогой дневник, мне не подобрать слов, чтобы описать боль и унижение, которое я испытал.",
    "Ты и ДжоДжо уже целовались? Ещё нет, так ведь? Твой первый поцелуй принадлежит не ему! Это был я, Дио!",
              "Я РУССКИЙ!!!",
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

def abFunc(pl):
    print("Кстати вот документы об отчислении спидозный.")
    pl.inventory.Add(Ithem("Заявление на Отчисление","Пиздуй работать дворником нищий",0))



def main():
    randfomNameConsole()
    os.system("cls")
    logo()
    input("Enter any key to start....")
    os.system("cls")
    pl = Player('Player', 0)

    sceneTest = Scene(5,3)
    sceneTest.Insert(pl.char, Point(0,0),pl)

    abramov = Person("Abramov",0,10,char='ab')
    enemy = Person("Enemy",2,20,char='e')
    dummy = Person("Dummy",2,10,char='d')

    abramov.inter.AddInteraction(Interact("say","А я Абрамов, и я изпользую другой пиздатый спрайт "+colored("гуччи","yellow"),True,func=abFunc))
    enemy.inter.AddInteraction(Interact("say","Я сосу хуй со стандартный спрайтом противника",False))

    sceneTest.Insert("grace",Point(5,0),collision=False)
    sceneTest.Insert(enemy.char, Point(2, 0), enemy, True, collision=True)
    sceneTest.Insert(abramov.char, Point(8, 1), abramov, True, collision=True)

    sceneTest.AddSprite(Sprite("ab", [" ┏┓  ", " ┛╹╹┗", "█████"]))
    sceneTest.AddSprite(Sprite("grace", ["-v---", "----v", "v----"]))
    sceneTest.AddSprite(Sprite("Abramov_fightscene",[
"""
---------=========------------------------------------------
----------========------------------------------------------
============-------------=----------------------------------
=============-==-------------------------------------------:
===================--------+##+-------------::::::::::::::::
=====================-----=*###=-------:::::::::::::::::::::
===========================*#%#====----------:::::::::::::::
========================+*#*+=========----------:::::----:::
==================-===**----==+++*+==-----------------------
===================-==----#=*+#*#***==--::::------==========
::---------------------*%+=**+*+#+*++:-=:::::::-------------
--------------:::::---*+=#=*+=+=+=+%*::::::::----:::::::::::
==-------------::::-+*=:-#+++=+===+*---:::::::::::::::::::::
============---::::===++#%+*+=+=-=----::-:::::::::::::::::::
+++++=======-------==**#%#++=----==*+----:::::::::::::::::::
++++++++++====------+=-=+**++=======+=----::::::::::::::::::
++###****####*+++=-=*##**=-+##*#*%@*=++=======+===--=++*#***
+++++==+*********#+-=%%+++*%%@@%#%@%++****+++*#*****##****++
++++++++++++++++++=-+%%+=+**+#%##%%%*=++****************+***
+++++======+++++++=-+%#==**+*++*#%%%*=*###***+***+++++++====
--------:-========-:*%#==*#=----#%%%*----==========---------
---=======-----=+++=*#*==++++++++****+*************+++++===-
===-=--------========----------------==============++****++*
========-===-====------------------====-=-------------=====+
=====----=======------------=++=-----:::::--=++=============


"""]))

    while(True):
        if pl.health <= 0:
            print("Game Over")
            return

        if sceneTest.GetPlayer().state == 0 :
            sceneTest.PrintMap()
            sceneTest.PlController()

        elif sceneTest.GetPlayer().state == 1 :
            action_pl = sceneTest.PlFight()
            action_bot = FightBot(pl,sceneTest.enemyFight)
            print(action_bot)
            sceneTest.FightAction(action_bot,pl,sceneTest.enemyFight)
            input()
            sceneTest.FightAction(action_pl, sceneTest.enemyFight, pl)
            input()

        time.sleep(0.1)
        os.system("cls")
main()