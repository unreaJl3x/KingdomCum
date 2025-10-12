import random
import os
from Scene.SceneController import *
from Scene.map import *
from Scene.bot import *
from Scene.Person.Inventory import Ithem
import time

def knightDiolog(param):
    l=[]
    for i in param:
        l.append(i)
    l[0].inventory.Add(Ithem("end","",0))

def chapterThree(pl:Player):
    sceneMain = Scene(5,3)
    sceneMain.Insert(pl.char, p=Point(0,0),obj=pl)


    knight = Person(name=("Дух рыцаря"),race = 0, aggresive= 2, char= "k" )
    sceneMain.Insert(char=knight.char, p=Point(6,0),obj=knight,canInter=True,collision=True)
    sceneMain.AddSprite(Sprite(knight.char,["✹✹✹  ","✹✹✹ ","✹✹✹  "]))
    knight.inter.AddInteraction(Interact("iaca", ""+colored("Носитель Хрустальной Розы… ты пробудил её истинную силу","cyan") + "" +"\n "+
                                                                                                colored("Но будь готов: с этого дня твоя жизнь принадлежит не только тебе, но и самой Этернии","cyan") + "" +"\n"+
                                                                                                " Принц попытался заговорить, но слова утонули в пустоте. Воин продолжал:" +"\n " +
                                                                                                colored("Впереди тебя ждут испытания. Реликвия дарует могущество, но потребует цену","cyan") + "" +"\n " +
                                                                                                colored("Твоё королевство возрождается, но вместе с ним пробуждаются и враги, которых забыли даже боги","cyan") + "\n" +
                                                                                                " В тот же миг хрустальный цветок распался, и в пустоте возникло видение:" +
                                                                                                "\n тёмные земли, над которыми возвышается башня, опутанная чёрными цепями. " +
                                                                                                "\n На её вершине горел мрачный свет, напоминающий искажённый кристалл Этернии." +
                                                                                                "\n От башни исходила такая же энергия, что и от метки принца, но тёмная, извращённая." +
                                                                                                "\n " + colored("Там источник будущей беды», произнёс голос. И там тот, кого ты видел во сне. Он идёт за тобой","cyan"),True,knightDiolog, pl))
    os.system("cls")
    print(
            colored("   (       )","red")+colored("                  )                )  ","yellow")+"\n"+
            colored("   )\\   (","yellow")+colored(" /(     )         ( /(","red")+colored("   (   (     ( /(  ","yellow")+"\n"+
            colored(" (((_)  ","red")+colored(")\\()) (","yellow")+colored(" /(  `  )   )","red")+colored("\\()) ))\\  )(   ","yellow")+colored(" )\\())","red")+"\n"+
            colored(" )\\___ (","yellow")+colored("(_)\\ ","red")+colored(" )(_)","yellow")+colored(") /(/( ","red")+colored(" (_))/ /((_)((","yellow")+colored(")\\  ((_)\\  ","red")+"\n"+
            colored("((","red")+"/ __|| |"+colored("(_)","red")+colored("((_)_ ((_)_\\ ","yellow")+"| |_"+colored(" (_))   ((","red")+""+colored("_)","yellow")+ " |__ (_)"+"\n"+
            " | (__ | ' \\ / _` || '_ \\)|  _|/ -_) | '_|  |_ \\   "+"\n"+
            "  \\\\___||_||_|\\\\__,_|| .__/  \\\\__|\\\\___| |_|   |___/   "+"\n"+
            "                   |_|                            ")
    print(
        "Обычные дни проходили мимо, рабочие закончили реставрировать город полностью, город становился еще оживление,"
        "\n а во дворце веяло приятно атмосферой. Лучи пробивались через шторы в покои принца. ")
    input("...")
    print("\n Утро проходило как обычно-принц просыпался, завтракал и уходил работать в кабинет, "+ colored("но что-то тревожило его.","yellow")+"")

    print("С каждым днем его "+ colored("отметка розы на руке становилась все ярче","cyan")+""
    "\n а сны все страннее и реалистичнее. Принц стал посещать тренировочные площадки все чаще,"
    "\n его сила росла, но ее становилось все сложнее контролировать.")
    input("...")
    print("После обычного вечернего разговора с "+ colored("Артанис V","yellow")+"он отправился в свои покои."
    "\n Ночью его мучали кошмары про будущее королевства и одного человека. "
    "\n Он был знаком принцу- его силуэт, его голос и фигура, но его лицо было размыто. "
    "\n Принц проснулся ночью в холодном поту, его метка розы стала настолько яркой,"
    "\n начала освещать всю комнату. От нее тянулись тусклые линии к рапире, чем ближе принц подходил к ней,"
    "\n тем виднее становились полосы.")
    input("...")
    print("Взяв ее в руки, его сознание перенеслось в нее. Сознание принца погрузилось в темноту. "
    "\n Вокруг не было ни стен, ни потолка, лишь бесконечная пустота, которую разрывали голубые искры."
    "\n Постепенно они сложились в очертания огромного цветка розы, сделанной из света и хрусталя. "
    "\n В центре цветка стоял силуэт — "+ colored ("высокий воин в доспехах, с лицом","cyan")+"скрытым под шлемом. "
    "\n Его голос прозвучал гулко, будто из глубины веков.")

    input("....")

    while(True):
        if pl.inventory.HaveIs("end"): return
        if pl.health <= 0:
            print("Game Over")
            break

        if sceneMain.GetPlayer().state == 0 :
            sceneMain.PrintMap()
            sceneMain.PlController()

        elif sceneMain.GetPlayer().state == 1 :
            action_pl = sceneMainPlFight()
            action_bot = FightBot(pl,sceneMain.enemyFight)
            #print(action_bot)
            scene.FightAction(action_bot,pl,sceneMain.enemyFight)
            input()
            scene.FightAction(action_pl, sceneMain.enemyFight, pl)
            input()

        time.sleep(0.1)
        os.system("cls")