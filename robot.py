from weapon import Weapon
class Robot:
    def __init__(self, name):
        self.name = name
        self.active_weapon = Weapon(self)
        self.health = 100
   
    def attack(self, dinosaur):
        pass

