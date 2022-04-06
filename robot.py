import random
from weapon import Weapon
ags = Weapon("Armadyl Godsword", 50)
dds = Weapon("Dragon dagger", 50)
d_claws = Weapon("d claws", 50)
weapon_list = [ags, dds, d_claws]

class Robot:
    def __init__(self, name):
        self.name = name
        self.active_weapon = random.choice(weapon_list)
        self.health = 100
        self.fleet = []
        
   
    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        return dinosaur.health

    def attack_random_weapon(self, dinosaur):
        self.active_weapon = random.choice(weapon_list)
        dinosaur.health -= self.active_weapon.attack_power

    def attack_random(self, random_player):
        random_player.health -= self.active_weapon.attack_power
        return random_player.health

        