class Inventory:
    def __init__(self, slotCount:int):
        self.slots = []
        self.max = slotCount
class Ithem:
    def __init__(self, name : str, description : str, type : int):
        self.name = name
        self.description = description
        self.type = type
class Weapon(Ithem):
    def __init__(self, name : str, description : str,damage:int):
        Ithem.__init__(self,name,description,"Weapon")
        self.damage = damage