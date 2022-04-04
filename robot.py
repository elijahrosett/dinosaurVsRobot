from weapon import Weapon
class Robot:
    def __init__(self, name):
        self.name = name
        self.active_weapon = ags
        self.attack_power = self.active_weapon.attack_power
        self.health = 100
   
    def attack(self, dinosaur):
        dinosaur.health -= self.attack_power
        return dinosaur.health

ags = Weapon("armadyl Godsword", 17)