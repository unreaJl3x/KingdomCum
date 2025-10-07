from src.Scene.map import Map
from src.kingdomdef import *
from termcolor import colored
import os

class Scene:
    def __init__(self):
        self.map = Map(sizeX=5,sizeY=3)
        self.__interacts__ =  list()
        self.__interacts__.append("WALK [w/a/s/d]")
        #self.__interacts__.append("ROTATE [a/d]")
        self.__interacts__.append("INTERACT WITH OBJECT [e]")

    def PlController(self):
        #for i in range(os.get_terminal_size().columns): print("█")
        print("████████████████████████████████████████")
        print("▪   ▐ ▄ ▄▄▄▄▄▄▄▄ .▄▄▄   ▄▄▄·  ▄▄· ▄▄▄▄▄\n██ •█▌▐█•██  ▀▄.▀·▀▄ █·▐█ ▀█ ▐█ ▌▪•██\n▐█·▐█▐▐▌ ▐█.▪▐▀▀▪▄▐▀▀▄ ▄█▀▀█ ██ ▄▄ ▐█.▪\n▐█▌██▐█▌ ▐█▌·▐█▄▄▌▐█•█▌▐█ ▪▐▌▐███▌ ▐█▌·\n▀▀▀▀▀ █▪ ▀▀▀  ▀▀▀ .▀  ▀ ▀  ▀ ·▀▀▀  ▀▀▀ ")
        print("████████████████████████████████████████")
        for i in self.__interacts__ :  print(colored(i,"green"))

        choice = input()
        match choice.lower():
            case "w":
                self.map.Move(Point(1,1),Point(1,1))
            case "a":
                self.map.Move(Point(1, 1), Point(1, 1))
            case "s":
                self.map.Move(Point(1, 1), Point(1, 1))
            case "d":
                self.map.Move(Point(1,1),Point(1,1))
            case "e":
                print(self.map.GetObj(Point(1,1)))
    def PrintMap(self):
        self.map.print()
