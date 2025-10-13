class Ithem:
    def __init__(self, name : str, description : str=None, type : int=0,count:int = 1, invisible:bool=False, func=None, *param):
        self.name = name
        self.description = description
        self.type = type
        self.count =count
        self.invisibledToPrint = invisible
        self.func = func
        self.param = param
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
    def __getitem__(self, ithem:int):
        if  self.slots[ithem].invisibledToPrint: return None
        return self.slots[ithem]

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
            if not self.slots[i].invisibledToPrint:
                print(f"(pos{i})(count{self.slots[i].count})"+self.slots[i].name,end="")
        print()

    def HaveIs(self,name:str)->bool:
        for i in self.slots:
            if i.name == name:
                return True
        return False
    def Use(self, choice:int):
        self.slots[int(choice)].func(self.slots[int(choice)].param)
