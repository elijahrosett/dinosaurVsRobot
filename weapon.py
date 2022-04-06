import random


class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = random.randrange(attack_power) 

    