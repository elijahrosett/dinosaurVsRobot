import random
from robot import Robot
todd = Robot("Todd")
eugene = Robot("Eugene")
jarvis = Robot("Jarvis")

class Fleet:
    def __init__(self, name, list):
        self.name = name
        self.list = list
        self.total_health = []
        self.attack = sum([])
        self.random_member = random.choice(list)
        
        
        
        

    def fleet_health(self, list):
        for items in list:
            self.total_health.append(items.health)
            total_health = sum(self.total_health)
        return total_health


    def attack_random_player(self, list):
        target = random.choice(list)
        target.health -= self.active_weapon.attack_power
        return target.health
    def pop_member(self, member):
        self.list.pop(member)
        return member
