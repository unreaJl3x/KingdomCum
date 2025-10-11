from .Entity import *
from .Attributes import *
from .Inventory import Inventory

"""Races: 0- Human; 1- Elf, 2- Orc"""
class Person(Entity):
    __directionForward__ = 0
    __directionBack__ = 1
    __directionRight__ = 2
    __directionLeft__ = 3

    __stateStable__ = 0
    __stateFight__ = 1
    __stateStory__ = 2

    __fightStateNull__ = 0
    __fightStateDefense__ = 1
    __fightStateParry__ = 2
    __fightStateStunned__ = 3

    @staticmethod
    def __getStrStateOnInt__(state:int)->str:
        match state:
            case 0: return "stable"
            case 1: return "fight"
            case 2: return "story"
        return ""
    @staticmethod
    def __getRaceFromInt__(num: int) -> str:
        match num:
            case 0: return "Human"
            case 1: return "Elf"
            case 2: return "Orc"
        return ""

    def __maxHealth__(self)->int:
        return self.attributes.strenght*0.8

    def __init__(self, name : str, race : int, aggresive:int = 0, char:str="P"):
        Entity.__init__(self, name, char)
        self.aggresive = 0
        self.race = race
        self.point = None
        self.fightState = 0
        self.attributes = GetAttributeFromRaceId(self.race)
        self.evasion = self.attributes.agility/2
        self.health = self.__maxHealth__()
        self.mana = self.attributes.inttiligence/2
        self.state = 0
        self.skills = []
        self.lastDirection = self.__directionForward__
        self.inventory = Inventory(5)

    def __str__(self):
        return f"[Person][{self.__getStrStateOnInt__(self.state)}][watch: {self.DirectionToText()}] {self.name}({self.__getRaceFromInt__(self.race)}) "

    def DirectionToText(self)->str:
        match self.lastDirection:
            case Person.__directionLeft__:return "left"
            case Person.__directionRight__: return "right"
            case Person.__directionBack__:return "back"
            case Person.__directionForward__:return "forward"

    def AddInteraction(self, interactName:str, action:str):
        self.inter.AddInteraction(Interact(interactName,action))
