class Interact:
    def __init__(self, interactName:str, action:str, delAferUse:bool = False, func=None):
        self.name = interactName
        self.action = action
        self.work = False
        self.func = func
        self.work = True
        self.delAferUse = delAferUse


    def __str__(self):
        return f"{self.name}"

class InteractionController:
    def __init__(self):
        self.__interacts__ = list()
    def AddInteraction(self,interact:Interact):
        self.__interacts__.append(interact)

    def RemoveInteraction(self,interactName:str)->bool:
        for i in self.__interacts__:
            if i.name == interactName:
                self.__interacts__.remove(i)
                return True
        return False

    def Use(self, name:str,pl,pasteBefore:str="",pasteAfter:str="")->bool:
        for i in self.__interacts__:
            if i.name == name:
                print(pasteBefore+i.action+pasteAfter,end="")
                if i.func is not None: i.func(True,pl)
                if (i.delAferUse): self.__interacts__.remove(i)
                return True
        return False