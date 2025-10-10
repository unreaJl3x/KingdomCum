class Ithem:
    def __init__(self, name : str, description : str, type : int,count:int = 1):
        self.name = name
        self.description = description
        self.type = type
        self.count =count
    def __str__(self):
        return f"({self.name}, {self.type}) {self.description}."

class Weapon(Ithem):
    def __init__(self, name : str, description : str,damage:int):
        Ithem.__init__(self,name,description,"Weapon")
        self.damage = damage

class Inventory:
    def __init__(self, slotCount:int):
        self.slots = []
        self.max = slotCount

    def Add(self, ithem:Ithem)->bool:
        for i in self.slots:
            if i.name == ithem.name or len(self.slots) >= self.max:
                return False
        self.slots.append(ithem)
        return True


    def Remove(self,name:str):
        for i in self.slots:
            if i.name == name:
                self.slots.remove(i)
                return True
        return False

    def print(self, sizeLine:int = 5):
        for i in range(len(self.slots)):
            if i%sizeLine == 0:
                print()
            print(self.slots[i].name+f" {self.slots[i].count}",end="")
        print()


