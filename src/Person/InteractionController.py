class Interact:
    def __init__(self,interactName:str, action:str, locked:bool = False):
        self.interactName = interactName
        self.action = action
        self.locked = locked
    def __str__(self):
        return f"{self.interactName}"

class InteractionController:
    def __init__(self):
        self.__interacts__ = list()
    def AddInteraction(self,interact:Interact):
        self.__interacts__.append(interact)
    def RemoveInteraction(self,interact:Interact):
        self.__interacts__.remove(interact)