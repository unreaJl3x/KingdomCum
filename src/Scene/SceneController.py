from src.Scene.map import Map
from src.kingdomdef import *
from termcolor import colored
from src.player import *
import os

class Scene:
    def __init__(self,sizeX:int =5,sizeY:int =3):
        self.map = Map(sizeX,sizeY)
        pl = Player("pl",0)
        self.map.Insert(pl.char,Point(0,0),obj=pl)
        #self.map.print()
        self.__interacts__ =  list()
        self.__interacts__.append("WALK [w/a/s/d]")
        #self.__interacts__.append("ROTATE [a/d]")
        self.__interacts__.append("INTERACT WITH OBJECT [e]")
        self.__interacts__.append("FIGHT [f]")

    @staticmethod
    def GetPointOnDirection(dir:int)->Point:
        match dir:
            case Person.__directionLeft__: return Point(-1,0)
            case Person.__directionRight__: return Point(1,0)
            case Person.__directionBack__: return Point(0,1)
            case Person.__directionForward__: return Point(0,-1)

    def PlController(self):
        #for i in range(os.get_terminal_size().columns): print("█")
        print("████████████████████████████████████████")
        print("▪   ▐ ▄ ▄▄▄▄▄▄▄▄ .▄▄▄   ▄▄▄·  ▄▄· ▄▄▄▄▄\n██ •█▌▐█•██  ▀▄.▀·▀▄ █·▐█ ▀█ ▐█ ▌▪•██\n▐█·▐█▐▐▌ ▐█.▪▐▀▀▪▄▐▀▀▄ ▄█▀▀█ ██ ▄▄ ▐█.▪\n▐█▌██▐█▌ ▐█▌·▐█▄▄▌▐█•█▌▐█ ▪▐▌▐███▌ ▐█▌·\n▀▀▀▀▀ █▪ ▀▀▀  ▀▀▀ .▀  ▀ ▀  ▀ ·▀▀▀  ▀▀▀ ")
        print("████████████████████████████████████████")
        for i in self.__interacts__ :  print(colored(i,"green"), end=";  ")

        choice = input()

        pl = self.map.Find(char=self.map.__charPlayer__.char)
        print(pl[0])
        if (len(pl)<2) : print("Player not found");return
        else: print(pl[1])
        match choice.lower():
            case "w":
                print(self.map.Move(pl[0], Point(pl[0].x,pl[0].y-1)))
            case "a":
                print(self.map.Move(pl[0], Point(pl[0].x-1,pl[0].y)))
            case "s":
                print(self.map.Move(pl[0], Point(pl[0].x,pl[0].y+1)))
            case "d":
                print(self.map.Move(pl[0], Point(pl[0].x+1,pl[0].y)))


        match choice.lower():
            case "f": print("1")

            case "e":
                point = Point(pl[0].x + self.GetPointOnDirection(pl[1].obj.lastDirection).x,
                              pl[0].y +self.GetPointOnDirection(pl[1].obj.lastDirection).y
              )
                if (point.x+point.y*self.map.sizeX<0 and point.x+point.y*self.map.sizeX>self.map.sizeX*self.map.sizeY+1): print("Cant use");return
                #if (self.map.map[point.x+point.y*self.map.sizeX].interacteble): print("U cant interact wich this object...")
                obj = self.map.map[point.x+point.y*self.map.sizeX].obj
                print(point)
                print(pl[1].obj)
                print("obj", self.map.map[point.x+point.y*self.map.sizeX])
                if (type(obj)==Person):
                    for i in obj.inter.__interacts__:
                        print(i,end="; ")
                    print()
                else: print("Nothing.....")
                input()

    def PrintMap(self):
        emptyChar  = [ "┏━━━┓", "┃   ┃", "┗━━━┛" ]
        playerChar = [ "## ##", "#####", "  #  " ]
        enemyChar  = [ "^^^^^", "_ | _", "|   |"]
        errChar    = [ "#####", "#####", "#####"]

        layer = 0
        line = 0
        ithem = 0
        messege = []
        while(True):
            if (self.map.map[ithem] == self.map.__charEmpty__):
                messege.append(emptyChar[layer]+" ")
            elif (self.map.map[ithem].char == self.map.__charPlayer__.char):
                messege.append(playerChar[layer]+" ")
            elif (self.map.map[ithem].char == self.map.__charEnemy__.char):
                messege.append(enemyChar[layer]+" ")
            else:
                messege.append(errChar[layer] + " ")

            if (len(messege)%self.map.sizeX==0):
                if ((len(messege)//self.map.sizeX)%len(emptyChar)==0):
                    line += 1
                ithem=line*self.map.sizeX-1
                layer += 1
                if (layer>=len(emptyChar)):layer=0
            ithem+=1
            if (ithem >= len(self.map.map)): break

        for i in range(len(messege)):
            if(i%self.map.sizeX==0):print()
            print(messege[i],end="")
        print("\n")

    def DrawFidhtScene(self):
        print("hui")