from .InteractionController import *
class Entity:
    def __init__(self,name : str, char:str):
        self.name = name
        self.inter = InteractionController()
        self.char = char