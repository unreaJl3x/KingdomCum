class Attributes:
    def __init__(self, strenght : int, agility : int, inttiligence : int):
        self.strenght = strenght
        self.agility = agility
        self.inttiligence = inttiligence

    def __add__(self, attr):
        self.strenght += attr.strenght
        self.agility += attr.agility
        self.inttiligence += attr.inttiligence

def GetAttributeFromRaceId(num:int)-> Attributes:
    match num:
        case 0:
            return Attributes(10,10,10)
        case 1:
            return Attributes(7, 12, 13)
        case 2:
            return Attributes(14, 8, 0)
    return Attributes(0, 0, 0)

def GetAttributeAddact(num:int)->Attributes:
    match num:
        case 0:
            return Attributes(5,5,5)
        case 0:
            return Attributes(3, 6, 7)
        case 0:
            return Attributes(15, 3, 1)
    return Attributes(0, 0, 0)