from src.Scene.map import Map
from src.kingdomdef import *
from termcolor import colored
import os

class Scene:
    def __init__(self):
        self.map = Map(sizeX=15,sizeY=23)
        self.__interacts__ =  list()
        self.__interacts__.append("WALK [w/a/s/d]")
        #self.__interacts__.append("ROTATE [a/d]")
        self.__interacts__.append("INTERACT WITH OBJECT [e]")

    def PlController(self):
        #for i in range(os.get_terminal_size().columns): print("█")
        print("████████████████████████████████████████")
        print("▪   ▐ ▄ ▄▄▄▄▄▄▄▄ .▄▄▄   ▄▄▄·  ▄▄· ▄▄▄▄▄\n██ •█▌▐█•██  ▀▄.▀·▀▄ █·▐█ ▀█ ▐█ ▌▪•██\n▐█·▐█▐▐▌ ▐█.▪▐▀▀▪▄▐▀▀▄ ▄█▀▀█ ██ ▄▄ ▐█.▪\n▐█▌██▐█▌ ▐█▌·▐█▄▄▌▐█•█▌▐█ ▪▐▌▐███▌ ▐█▌·\n▀▀▀▀▀ █▪ ▀▀▀  ▀▀▀ .▀  ▀ ▀  ▀ ·▀▀▀  ▀▀▀ ")
        print("████████████████████████████████████████")
        for i in self.__interacts__ :  print(colored(i,"green"), end=";  ")
        choice = input()

        pl = self.map.Find(char=self.map.__charPlayer__)
        match choice.lower():
            case "w":
                print(self.map.Move(pl[0], Point(pl[0].x,pl[0].y-1)))
            case "a":
                print(self.map.Move(pl[0], Point(pl[0].x-1,pl[0].y)))
            case "s":
                print(self.map.Move(pl[0], Point(pl[0].x,pl[0].y+1)))
            case "d":
                print(self.map.Move(pl[0], Point(pl[0].x+1,pl[0].y)))
            case "e":
                print(self.map.GetObj(Point(1,1)))

    def PrintMap(self):
        ithem = 0
        messege = []
        emptyChar  = [ "┏━━━┓", "┃   ┃", "┗━━━┛" ]

        playerChar = [ "┗━ ━┛", "  ┃  ", "  ┃  " ]
        layer = 0
        line = 0
        while(True):
            #print(len(messege))
            if (self.map.map[ithem] == self.map.__charEmpty__):
                messege.append(emptyChar[layer]+" ")
                #print("i->",ithem)
            elif (self.map.map[ithem] == self.map.__charPlayer__):
                messege.append(playerChar[layer]+" ")

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

