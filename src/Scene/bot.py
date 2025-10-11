import random
from .Person.Person import *

def __chance(chance:float, min:float,max:float): return chance > min and chance < max

def FightBot(pl:Person,me:Person)->str:
    if me.health/me.__maxHealth__() <= 0.3*me.__maxHealth__():
        if me.evasion > pl.evasion:
            return "p"

    chance = random.randint(0,10)/10
    chance_attack = 0.5
    chance_defense = 0.3

    if pl.attributes.strenght <= me.attributes.strenght: chance_attack +=0.15
    elif pl.attributes.strenght > me.attributes.strenght: chance_attack-=0.21; chance_defense+=0.21
    print(f"Chance attack ({chance_attack}), defensse ({chance_defense}), rolled {chance}")
    if __chance(chance, -1, chance_attack):
        return 'q'
    elif __chance(chance, chance_attack+0.01, chance_defense):
        return 'd'
    return "e"
