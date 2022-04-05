import random
from robot import Robot
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
        self.herd = []

    def attack(self, robot):
        robot.health -= self.attack_power
        return robot.health

    def attack_random(self, random_player):
        random_player.health -= self.attack_power
        return random_player.health
        
    def attack_random_player(self, list):
        target = random.choice(list)
        target.health -= self.attack_power
        return target.health
