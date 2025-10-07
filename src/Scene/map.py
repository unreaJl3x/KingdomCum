from src.kingdomdef import Point
from typing import Final

class MapPoint():
    def __init__(self,char:str,objName:str, inter:bool=False, obj = None):
        self.objName = objName
        self.char = char
        self.interacteble = inter
        self.obj = obj
    def __str__(self):
        return self.char

class Map:
    def __init__(self, sizeX:int, sizeY:int):
        self.map = list(range(sizeX*sizeY))
        self.sizeY = sizeX
        self.sizeX = sizeY

        self.__charChest__ = MapPoint(char="c", objName="chest")
        self.__charPlayer__ = MapPoint(char="p", objName="player")
        self.__charWall__ = MapPoint(char="#", objName="wall")
        self.__charEnemy__ = MapPoint(char="e", objName="enemy")
        self.__charEmpty__ = MapPoint(char="-", objName="empty")

        for i in range(sizeX*sizeY):
            self.map[i] = self.__charEmpty__

    def Move(self, posStart : Point, posEnd : Point) -> bool:
        print("q")

    def print(self):
        for i in range(len(self.map)):
            if (i%self.sizeY == 0):print("")
            print(self.map[i],end="")
        print("")

    def Find(self, char:str, count:int=0) -> Point:
        for i in range(len(self.map)):
            if (self.map[i] == char):
                return Point(i%self.sizeY, i//self.sizeY)
        return Point(-1,-1)

    """-1 -> all map"""
    def Clear(self, count:int=-1):
        for i in range(len(self.map)): self.map[i] = self.__charEmpty__

    def Insert(self, char:str, p:Point, isNull:bool=True)->bool:
        if (    (isNull and self.map[p.x+p.y*self.sizeX] != self.__charEmpty__) or
                        p.x + p.y*self.sizeY >= len(self.map)
        ): return False

        self.map[ p.x + p.y*self.sizeY ] = char
        return True

    def GetObj(self,p:Point):
        return self.map[p.x+p.y*self.sizeX].obj