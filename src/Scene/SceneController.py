import random
from unittest import case

from .player import *
from .map import *
from termcolor import colored
import os

class Sprite:
    def __init__(self, name:str,l:list):
        self.name = name
        self.list = l

"""plFov(4) - 4x4"""
class Scene:
    def __init__(self,sizeX:int =5,sizeY:int =3,plFov:int=4):
        self.map = Map(sizeX,sizeY)

        self.__interacts__ =  list()
        self.__interacts__.append("WALK [w/a/s/d]")
        self.__interacts__.append("INTERACT WITH OBJECT [e]")
        self.__interacts__.append(colored("FIGHT [f]",'red'))
        self.__interacts__.append("Inventory [i]")

        self.__fightInteract__ = list()
        self.__fightInteract__.append("Try Hit (q)")
        self.__fightInteract__.append("Defense (d)")
        self.__fightInteract__.append("Parry (e)")
        self.__fightInteract__.append("Hold (h)")
        self.__fightInteract__.append("Escape (p)")

        self.sprites = dict()
        self.plFov = plFov
        self.enemyFight = None

        self.AddSprite(Sprite('-', [".....", ".....", "....."]))
        self.AddSprite(Sprite('p', ["## ##", "#####", "  #  "]))
        self.AddSprite(Sprite("e", ["^^^^^", "_ | _", "|   |"]))
        self.AddSprite(Sprite("error", ["#####", "#####", "#####"]))
        self.spriteSize = len(self.sprites["error"].list)

    @staticmethod
    def GetPointOnDirection(dir:int)->Point:
        match dir:
            case Person.__directionLeft__: return Point(-1,0)
            case Person.__directionRight__: return Point(1,0)
            case Person.__directionBack__: return Point(0,1)
            case Person.__directionForward__: return Point(0,-1)

    def Insert(self, char:str, p:Point, obj = None, canInter:bool = False, collision:bool=False):
        return self.map.Insert(char, p, obj, canInter,collision=collision)

    def PlController(self):
        #for i in range(os.get_terminal_size().columns): print("█")
        print(colored("████████████████████████████████████████","cyan"))
        print(colored("▪   ▐ ▄ ▄▄▄▄▄▄▄▄ .▄▄▄   ▄▄▄·  ▄▄· ▄▄▄▄▄\n██ •█▌▐█•██  ▀▄.▀·▀▄ █·▐█ ▀█ ▐█ ▌▪•██\n▐█·▐█▐▐▌ ▐█.▪▐▀▀▪▄▐▀▀▄ ▄█▀▀█ ██ ▄▄ ▐█.▪\n▐█▌██▐█▌ ▐█▌·▐█▄▄▌▐█•█▌▐█ ▪▐▌▐███▌ ▐█▌·\n▀▀▀▀▀ █▪ ▀▀▀  ▀▀▀ .▀  ▀ ▀  ▀ ·▀▀▀  ▀▀▀ ","magenta"))
        print(colored("████████████████████████████████████████","cyan"))
        for i in self.__interacts__ :  print(i, end=";  ")

        choice = input()

        pl = self.map.Find(char=self.map.__charPlayer__.char)
        if (len(pl)<2) : print("Player not found");return
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
            case "f":
                point = self.map.PointToInt(pl[0]+self.GetPointOnDirection(pl[1].obj.lastDirection))
                obj = self.map.map[point].obj
                if type(obj) == Person:
                    obj.point = point
                    self.enemyFight = obj
                    pl[1].obj.state = Person.__stateFight__
                    os.system("cls")

                else:
                    print("Nothing....")
                    input()

            case "e":
                point = Point(pl[0].x + self.GetPointOnDirection(pl[1].obj.lastDirection).x,
                              pl[0].y +self.GetPointOnDirection(pl[1].obj.lastDirection).y
              )
                print(type(self.map.map[self.map.PointToInt(point)].obj))
                if self.map.PointToInt(point)<0 or self.map.PointToInt(point) > len(self.map.map): print("Cant use");input();return
                obj = self.map.map[self.map.PointToInt(point)].obj
                print(f"\nActions wich "+colored(f"[{obj.name}];","yellow"))


                if (len(obj.inter.__interacts__)==1):
                    obj.inter.Use(obj.inter.__interacts__[0].name, pasteBefore=colored(f"[{obj.name}] ","yellow"),pasteAfter="....\n")
                else:
                    for i in obj.inter.__interacts__:
                        print("",i,end=" ")
                    print()
                    choice = input()
                    if not obj.inter.Use(choice, pasteBefore=colored(f"[{obj.name}]: ","yellow"),pasteAfter="....\n"): print(f"U cannot do '{choice}'")

                print()

                input()

            case "i":
                os.system("cls")
                print(  "███████████████████████████\n"+
                        " ▄▀▀█▄▄   ▄▀▀█▄   ▄▀▀▀▀▄ \n"  +
                        "▐ ▄▀   █ ▐ ▄▀ ▀▄ █  \n"       +
                        "  █▄▄▄▀    █▄▄▄█ █    ▀▄▄ \n" +
                        "  █   █   ▄▀   █ █     █ █ \n"+
                        " ▄▀▄▄▄▀  █   ▄▀  ▐▀▄▄▄▄▀ ▐ \n"+
                        "█    ▐   ▐   ▐   ▐         \n"+
                        "▐                          \n" +
                        "███████████████████████████\n"
                )
                pl[1].obj.inventory.print()
                print("\nMayby inspect any ithem?(num)")
                choice = input()
                try:
                    print(pl[1].obj.inventory.slots[int(choice)])
                except:
                    print("Nothing.....")
                input()

    def PrintMap(self):
        layer = 0
        line = 0
        ithem = 0
        messege = []

        while(True):
            if (self.map.map[ithem].char in self.sprites):
                messege.append((self.sprites[self.map.map[ithem].char].list)[layer]+" ")
            else:
                messege.append(self.sprites["error"].list[layer] + " ")

            if (len(messege)%self.map.sizeX==0):
                if ((len(messege)//self.map.sizeX) % self.spriteSize==0):
                    line += 1
                ithem = line*self.map.sizeX-1
                layer += 1
                if (layer >= self.spriteSize):layer=0
            ithem+=1
            if (ithem >= len(self.map.map)): break

        for i in range(len(messege)):
            if(i%self.map.sizeX==0):print()
            print(" ",messege[i],end="")
        print("\n")

    def GetPlayer(self) -> Player | None:
        pl = self.map.Find(char=self.map.__charPlayer__.char)
        #print(pl[0])
        if (len(pl)<2) : print("Player not found");return None
        return pl[1].obj

    def AddSprite(self, sprite:Sprite):
        self.sprites[sprite.name] = sprite

    def RemoveSprite(self, spriteName:str):
        del self.sprites[spriteName]

    def __win(self, pl:Player):
       # os.system("cls")
        print(self.enemyFight.point)
        input()
        pl.state = Person.__stateStable__
        self.map.Insert('-', Point(self.enemyFight.point,0))
        self.enemyFight = None

    def FightAction(self,act:str, target:Person, user:Person):
        if user.fightState == user.__fightStateStunned__:
            user.fightState = user.__fightStateNull__
            return
        match act.lower():
            case "q":
                print(f"{user.name} attack {target.name}.",end=" ")
                chance = (((target.evasion * 0.85) / user.evasion) * (random.randrange(0, 8) / 8)) * 1.24

                if chance > 0.215:
                    if target.fightState == target.__fightStateParry__:
                        target.fightState = target.__fightStateNull__
                        user.fightState = target.__fightStateStunned__
                        print(f"{user.name} is STUNNED.")
                        input()

                    hitDmg = (user.attributes.strenght / target.attributes.strenght) * random.randint(0, 5) / 2
                    if target.fightState == Person.__fightStateDefense__: hitDmg = hitDmg*((user.attributes.strenght / target.attributes.strenght)*random.randint(1,5)/5)
                    target.health -= hitDmg
                    print(f"and hit on {hitDmg}",end="")
                    print()
                    if int(target.health) <= 0:
                        print(f"{target.name} DIE.")
                        input()
                        self.__win(user)
                else: print(f"and miss :) {target.name} under protection Hakari")
            case "d":
                print(f"{user.name} becomes protective",end=" ")
                user.fightState = user.__fightStateDefense__
            case "e":
                print(f"{user.name} raddy to parry.")
                user.fightState = user.__fightStateParry__
                return
            case "h": print(f"{user.name} waiting youre action")

        if user.fightState == Person.__fightStateParry__:
            user.fightState = user.__fightStateStunned__

    """name_fightscene sprite"""
    def PlFight(self)->str:
        pl = self.GetPlayer()

        if f"{self.enemyFight.name}_fightscene" in self.sprites.keys():
            request = f"{self.enemyFight.name}_fightscene"
        elif f"{self.enemyFight.char}" in self.sprites.keys():
            request = self.enemyFight.char
        else: request = "error"

        for i in self.sprites[request].list:
            print("               "+i)
        print(f"    [{self.enemyFight.name}] have health {int(self.enemyFight.health)}")
        print(f"    [ You ] have health {int(pl.health)}")

        print( colored(
               "█████████████████████████████████\n"+
               "  ▄████  ▄█   ▄▀   ▄  █    ▄▄▄▄▀ \n" +
               "  █▀   ▀ ██ ▄▀    █   █ ▀▀▀ █ \n" +
               " █▀▀    ██ █ ▀▄  ██▀▀█     █ \n" +
               "  █      ▐█ █   █ █   █    █ \n" +
               "   █      ▐  ███     █    ▀ \n" +
               "    ▀               ▀          \n" +
               "█████████████████████████████████" ,"red" ))
        for i in self.__fightInteract__:
            print(""+i,end="; ")
        print()

        return input()