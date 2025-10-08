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
        self.sizeY = sizeY
        self.sizeX = sizeX

        self.__charChest__ = MapPoint(char="c", objName="chest")
        self.__charPlayer__ = MapPoint(char="p", objName="player")
        self.__charWall__ = MapPoint(char="#", objName="wall")
        self.__charEnemy__ = MapPoint(char="e", objName="enemy")
        self.__charEmpty__ = MapPoint(char="-", objName="empty")

        for i in range(sizeX*sizeY):
            self.map[i] = self.__charEmpty__

    def Move(self, posStart : Point, posEnd : Point) -> bool:
        if (posEnd.x+posEnd.y*self.sizeX <0 or posEnd.x+posEnd.y*self.sizeX>self.sizeY*self.sizeX): return False
        if (self.map[posEnd.x+posEnd.y*self.sizeX]==self.__charEmpty__):
            a = self.map[posEnd.x+posEnd.y*self.sizeX]
            #print(posStart, " ", posStart.y*self.sizeX , " sum: ", posStart.x+posStart.y*self.sizeX , " char:", self.map[posStart.x+posStart.y*self.sizeX])
            self.map[posEnd.x+posEnd.y*self.sizeX] = self.map[posStart.x+posStart.y*self.sizeX ]
            self.map[posStart.x+posStart.y*self.sizeX] = a
            #print(a)
            return True

        return False

    def print(self):
        for i in range(len(self.map)):
            if (i%self.sizeY == 0):print("")
            print(self.map[i],end="")
        print("")
    """Bad request, return [point(-1,-1)], else [point, mapPoint]"""
    def Find(self, char:str, count:int=0) -> list():
        for i in range(len(self.map)):
            if (self.map[i] == char):
                return [Point(i%self.sizeX, i//self.sizeX), self.map[i]]
        return [Point(-1,-1)]

    """-1 -> all map"""
    def Clear(self, count:int=-1):
        for i in range(len(self.map)): self.map[i] = self.__charEmpty__

    def Insert(self, char:str, p:Point, obj = None, objName:str = None, canInter:bool = False)->bool:
        if (    (self.map[p.x+p.y*self.sizeX] != self.__charEmpty__) or
                        p.x + p.y*self.sizeY >= len(self.map)
        ): return False

        self.map[ p.x + p.y*self.sizeY ] =  MapPoint(char=char, objName=objName, inter=canInter, obj=obj)
        return True

    def GetObj(self,p:Point):
        return self.map[p.x+p.y*self.sizeX].obj