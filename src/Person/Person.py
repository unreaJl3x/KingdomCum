from src.kingdomdef import *

class Person:
    def __init__(self, name : str, race : int):
        self.name = name
        self.race = race
        self.attributes = GetAttributeFromRaceId(self.race)
        self.evasion = self.attributes.agility/2
        self.position = Point(0,0)
        self.state = 0
        self.skills = []

    def __str__(self):
        return f"[Person][{GetStateFromNum(self.state)}] {self.name}({GetRaceFromId(self.race)}) "