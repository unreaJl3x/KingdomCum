class Attributes:
    def __init__(self, strenght : int, agility : int, inttiligence : int):
        self.strenght = strenght
        self.agility = agility
        self.inttiligence = inttiligence

    def __add__(self, attr):
        self.strenght += attr.strenght
        self.agility += attr.agility
        self.inttiligence += attr.inttiligence