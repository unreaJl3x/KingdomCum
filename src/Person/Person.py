from src.kingdomdef import *
from src.Person.Entity import *

class Person(Entity):
    __directionForward__ = 0
    __directionBack__ = 1
    __directionRight__ = 2
    __directionLeft__ = 3

    def __init__(self, name : str, race : int, aggresive:int = 0, char:str="P"):
        Entity.__init__(self, name, char)
        self.aggresive = 0
        self.race = race
        self.attributes = GetAttributeFromRaceId(self.race)
        self.evasion = self.attributes.agility/2
        self.health = self.attributes.strenght/2
        self.mana = self.attributes.inttiligence/2
        self.state = 0
        self.skills = []
        self.lastDirection = self.__directionForward__

    def __str__(self):
        return f"[Person][{GetStateFromNum(self.state)}][watch: {self.DirectionToText()}] {self.name}({GetRaceFromId(self.race)}) "

    def DirectionToText(self)->str:
        match self.lastDirection:
            case Person.__directionLeft__:return "left"
            case Person.__directionRight__: return "right"
            case Person.__directionBack__:return "back"
            case Person.__directionForward__:return "forward"