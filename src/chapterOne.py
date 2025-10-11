
import random
import os
from Scene.SceneController import *
from Scene.map import *
from Scene.Person.Inventory import *
from Scene.bot import *
import time

def outside(scene:Scene,currentScene:Scene):
    pl = scene.GetPlayer()
    currentScene = scene
    currentScene.Insert(pl.char,Point(0,0),obj=pl)

def door(scene:Scene,currentScene:Scene):
    pl = scene.GetPlayer()
    currentScene = scene
    currentScene.Insert(pl.char,Point(0,0),obj=pl)

def chapterOne(pl:Player):
    scene= Scene(5,3)
    scene.Insert(pl.char, p=Point(0,0),obj=pl)
    sceneChoiceOne = Scene(5,3)

    butler = Person(name=("Дворецкий"),race = 0, aggresive= 2, char= "d" )
    scene.Insert(char=butler.char, p=Point(6,0),obj=butler,canInter=True,collision=True)
    scene.AddSprite(Sprite(butler.char,["^ ^  ","(﹀( ","###  "]))
    butler.inter.AddInteraction(Interact(interactName=("say"), delAferUse=True,action= ("“Здравствуйте, принц”- поклонился и снова пристально стал рассматривать вас "\
                                                                               "\n“как видите дела идут у нас не очень хорошо,"\
                                                                               "\n столица держится из последних сил, а самое главное, что семейную реликвию украли”."
                                                                               "\nУкрали святой меч, "+colored("Хрустальная роза,","magenta")+" рапира которая передавалась из поколения в поколение этому королевству. "
                                                                               "\n Хрустальная рапира, которая была прочнее любого алмаза и прекраснее любого цветка")))


    quest1 = Person(name=("quest 1"),race=0, aggresive=0, char= "q1" )
    scene.Insert(char=quest1.char, p=Point(4,0),obj=quest1,canInter=True,collision=True)
    scene.AddSprite(Sprite(quest1.char,[" ### "," #*#"," ### "]))
    quest1.inter.AddInteraction(Interact(interactName=("hui"), delAferUse=True,action= ("Вы попали в гробницу, хотите войти(y/n)"),func=door))

    quest2 = Person(name=("quest 2"),race=0, aggresive=0, char= "q2" )
    scene.Insert(char=quest2.char, p=Point(7,0),obj=quest2,canInter=True,collision=True)
    scene.AddSprite(Sprite(quest2.char,[" *** "," ***"," ▨▨▨ "]))
    quest2.inter.AddInteraction(Interact(interactName=("penis"), delAferUse=True,action= ("Вы пришли во дворец и сели за свой стол, хотите продолжить(y/n)"),func=outside))






    print(''' ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄          ▄▄▄▄     
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌       ▄█░░░░▌    
▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌      ▐░░▌▐░░▌    
▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌          ▐░▌       ▐░▌       ▀▀ ▐░░▌    
▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌          ▐░░▌    
▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌          ▐░░▌    
▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀▀▀      ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀           ▐░░▌    
▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▌  ▐░▌               ▐░▌     ▐░▌          ▐░▌     ▐░▌            ▐░░▌    
▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌      ▐░▌ ▐░▌               ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌       ▄▄▄▄█░░█▄▄▄ 
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌               ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀  ▀         ▀  ▀                 ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀       ▀▀▀▀▀▀▀▀▀▀▀ 
                                                                                                                          '''" " \
    "\nКогда человечество достигло вершины своего развития, государства начали соперничать не за землю и золото, а за энергию." \
    "\n В недрах планеты были обнаружены кристаллы "+colored("Этерния — источники безграничной силы","cyan")+", " \
    "\nспособные питать целые города и даже менять структуру материи. " \
    "\n Сначала страны заключили союз, чтобы совместно использовать новое открытие.Но алчность правителей и страх потерять власть разрушили этот союз. "
    "\nКаждый континент объявил Этерний своей собственностью, начались тайные разработки оружия, способного подчинять энергию кристаллов. "
    "\n Когда первый взрыв Этернии стер с лица земли столицу Экрасии, было уже поздно. Мир погрузился в хаос."
    "\n Союзы рухнули, армии восстали против своих командиров, города превратились в пепел. "
    "\n"+colored("Так началась Великая Война Этерния — война, что поглотила свет цивилизации и оставила лишь тени былого величия.",  "cyan")+" ")
    print( "\n После войны между государствами некоторые страны пришли в упадок, такие как "+colored("Волдайк, Амидония, Контарелла и другие.","cyan")+", " \
    "\n Это назвали всемирным кризисом. Вся королевская семья сгинула в небытие и остался лишь младший принц, "
    "\n пребывавший в этот момент на тренировках горах." \
    "\n Вернувшись увидев картину, которая очень сильно ударила его морально. "+colored("Он решил возродить свое королевство и сразиться даже с богами, для возвращения своего дома.","yellow")+", ")
    input(".....")

    while(True):
        if pl.health <= 0:
            print("Game Over")
            return

        if scene.GetPlayer().state == 0 :
            scene.PrintMap()
            scene.PlController()

        elif scene.GetPlayer().state == 1 :
            action_pl = scene.PlFight()
            action_bot = FightBot(pl,scene.enemyFight)
            print(action_bot)
            scene.FightAction(action_bot,pl,scene.enemyFight)
            input()
            scene.FightAction(action_pl, scene.enemyFight, pl)
            input()

        time.sleep(0.1)
        os.system("cls")


