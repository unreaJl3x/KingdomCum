from Person.Attributes import Attributes

def GetRaceFromId(num:int)->str:
    match num:
        case 0: return  "Human"
        case 1: return  "Elf"
        case 2:  return "Orc"
    return ""

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

class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def __add__(self, p):
        self.x += p.x
        self.y += p.y

    def __mul__(self, p):
        self.x *= p.x
        self.y *= p.y

    def __sub__(self, p):
        self.x -= p.x
        self.y -= p.y

    def __str__(self):
        return f"({self.x}, {self.y})"

def GetStateFromNum(num:int)->str:
    match num:
        case 0: return "stable"
        case 1: return "stunned"
    return ""