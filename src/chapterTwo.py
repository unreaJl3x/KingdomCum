import random
import os
from Scene.SceneController import *
from Scene.map import *
from Scene.bot import *
import time
from chapterOne import Document
from Scene.Person.Inventory import *

def setMap(param):
    if input() != "y":
        print("Решили остаться")
        return

    print("Вы прошли")
    l = []
    for i in param:
        l.append(i)
    l[0].map = l[1]
    pGet = l[0].map.Find(char=l[2].char)
    if (len(pGet)<2):
        l[0].Insert(l[2].char, l[3], obj=l[2])

documents = [
                Document("Торговые пути","С начала мы хотим провести между нашими странами торговые пути, для обмена вещами и продовольствием, как вы смотрите на это?",10),
                Document("Строение Моста","Предложение построить над рекой "+colored("Нил","cyan")+" мост, что без поддержки его состояния простоит около полувека. Так же необнократно приходили жалобы об нападок разбойников на наши караваны, мост мог бы решить эту проблему. Требует средств казны.",10),
                Document("Понижение Томожных Пошлин для государства ","Снижени товарных пошлин отразится на ценообразовании товаров первой потребности для наших граждан.",10),
                Document("Союз","Объединение с союзными государствами с целью взаимной помощи в войне.",10)
]
documents[1].message = "А второй вопрос заключается в том, чтобы провести мост над рекой между нашими странами, ведь людям так станет проще добираться и торговцам не придется проходить большое расстояние в горах. "
documents[2].message = "Первое. Таможенные пошлины. Они излишне высоки. Мы считаем их тормозом для нормальной торговли. Снижение тарифов выгодно обеим сторонам. Вопрос даже не в предложении, а в целесообразности. Поддержите вы это или нет — отразится, прежде всего, на ваших же торговцах.” "
documents[3].message = "Второе. Союзный договор. Взаимные обязательства в случае внешней угрозы. Это укрепит позиции обоих государств, но отказ будет сигналом слабости. Мы не настаиваем словами — факты сделают это за нас. Какую позицию займёте вы?”"

def CheckDocuments(param):
    l=[]
    for i in param:
        l.append(i)
    l[1].inventory.Add(Ithem(l[2]," "))
    for i in l[0]:
        os.system("cls")
        if i.message != None:
            print(i.message)
            input("....")
        print(f"                    [{i.header}]  \n   {i.text}\n Отклонить(n)        Согласиться(y)", end="")
        if input() != 'y':
            return
    input("Все предложения рассмотрены...")

def diologiWothAnime(param):
    l=[]
    for i in param:
        l.append(i)
    l[0].inventory.Add(Ithem(l[1]," ",0))
    print(colored("Тихо смеётся и смотря прямо тебе в глаза говорит:","cyan")+" ” Мне очень хотелось с вами поговорить, ведь говорят, что чрезвычайно умны и красивы, и обсудить пару вещей по политике”.")
    input("...")
    print(colored("Вы активно обсуждаете политическое положение двух стран и соглашаетесь на союз между вашими странами. Благодаря этому диалогу принц и королева оказались в выгодном положении. ","cyan"))
    input("...")
    print("После всех встреч Артанис V решила остаться во дворце, чтобы узнать побольше о этой стране и ее людях. Ночью, принц находился в саду и читал документы, пока к нему кто-то не подкрался и положил руки на его плечи.\n"+
    "Принц резко обернулся и увидел яркие глаза Артанис V за своей спиной. Она мягко улыбнулась и села рядом с принцем заведя разговор. Они общались всю ночь на пролет и стали намного ближе, не как король и королева разных стран, а как друг и подруга, учившиеся в одной школе."
)

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
    butler = Person("Дворецкий",0,0,'b')
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

    poslanets[0].inter.AddInteraction(Interact("say","Приветствую вас ваше высочество, меня зовут "+colored("Иларион","yellow")+", я представитель страны Сархана. Я бы хотел обсудить с вами два вопроса",True,CheckDocuments,documents[0:2],pl,"p1"))
    poslanets[1].inter.AddInteraction(Interact("say","Стосеул. Представитель государства Амидония. Буду говорить прямо, без лишних реверансов и балагурства.",True, CheckDocuments, documents[2:4],pl,"p2"))
    poslanets[2].inter.AddInteraction(Interact("say",None,True,diologiWothAnime,pl,"p3"))

    for i in range(len(poslanets)):
        throneHallMap.Insert(poslanets[i].char, Point(5,i+1),poslanets[i],True,True)


    print(

        colored("   (       )","red")+colored("                  )                )  ","yellow")+"\n"+
        colored("   )\\   (","yellow")+colored(" /(     )         ( /(","red")+colored("   (   (     ( /(  ","yellow")+"\n"+
        colored(" (((_)  ","red")+colored(")\\()) (","yellow")+colored(" /(  `  )   )","red")+colored("\\()) ))\\  )(   ","yellow")+colored(" )\\())","red")+"\n"+
        colored(" )\\___ (","yellow")+colored("(_)\\ ","red")+colored(" )(_)","yellow")+colored(") /(/( ","red")+colored(" (_))/ /((_)((","yellow")+colored(")\\  ((_)\\  ","red")+"\n"+
        colored("((","red")+"/ __|| |"+colored("(_)","red")+colored("((_)_ ((_)_\\ ","yellow")+"| |_"+colored(" (_))   ((","red")+""+colored("_)","yellow")+ " |_  )"+"\n"+
        " | (__ | ' \\ / _` || '_ \\)|  _|/ -_) | '_|  / /   "+"\n"+
        "  \\___||_||_|\\__,_|| .__/  \\__|\\___| |_|   /___|  "+"\n"+
        "                   |_|                            ")
    print("От войны не осталось и следа, здания были отреставрированы, улицы убраны, а люди спешили на работу.\n"+"Находясь в своем новом дворце, принц был очень доволен результатом.\n""Стоявший рядом дворецкий, увидел довольное лицо и в его груди что-то защемило, но он резко откинул все внутри себя и холодным голосом сказал принцу: \n\n")
    input(".....")

    scene.map = lobbyMap
    os.system("cls")
    while (True):
        if pl.inventory.HaveIs("p1") and pl.inventory.HaveIs("p2") and pl.inventory.HaveIs("p3"): return

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