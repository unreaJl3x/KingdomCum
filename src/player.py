from Person.Person import *
class Player(Person):
    def __init__(self, name : str, race : int):
        Person.__init__(self,name,race,char='p')

